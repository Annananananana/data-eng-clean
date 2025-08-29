import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName(os.getenv("SPARK_APP_NAME", "BitcoinETL"))
    .getOrCreate()
)

broker = os.getenv("KAFKA_BROKER", "redpanda:9092")
topic  = os.getenv("KAFKA_TOPIC", "bitcoin")

# --- 1) Kafka lesen (einmaliger Batch-Read via startingOffsets=earliest) ---
raw = (
    spark.read
    .format("kafka")
    .option("kafka.bootstrap.servers", broker)
    .option("subscribe", topic)
    .option("startingOffsets", "earliest")
    .load()
)

# value ist binär → in String wandeln und parsen: "YYYY-MM-DD,Close"
df = raw.select(F.col("value").cast("string").alias("line"))
df = df.select(
    F.to_date(F.split("line", ",").getItem(0), "yyyy-MM-dd").alias("date"),
    F.split("line", ",").getItem(1).cast("double").alias("close")
).dropna()

daily = (
    df.groupBy("date")
      .agg(F.avg("close").alias("avg_close"))
      .orderBy("date")
)

# --- 2) In Postgres schreiben ---
pg_url = f"jdbc:postgresql://{os.getenv('POSTGRES_HOST','postgres')}:{os.getenv('POSTGRES_PORT','5432')}/{os.getenv('POSTGRES_DB','bitcoin')}"
props = {
    "driver": "org.postgresql.Driver",
    "user": os.getenv("POSTGRES_USER", "user"),
    "password": os.getenv("POSTGRES_PASSWORD", "pass"),
}

(daily
 .write
 .mode("append")
 .jdbc(pg_url, "daily_avg", properties=props)
)

spark.stop()
