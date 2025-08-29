from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, avg

spark = SparkSession.builder.appName("BitcoinETL").getOrCreate()

df = spark.read.csv("/data/bitcoin_sample.csv", header=True, inferSchema=True)
df = df.withColumn("Date", to_date(col("Date")))
daily_avg = df.groupBy("Date").agg(avg(col("Close")).alias("avg_close"))

jdbc_url = "jdbc:postgresql://postgres:5432/bitcoin"
props = {"user": "user", "password": "password", "driver": "org.postgresql.Driver"}
daily_avg.write.mode("overwrite").jdbc(jdbc_url, "daily_avg", properties=props)

print("Wrote rows:", daily_avg.count())
spark.stop()
