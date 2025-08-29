import os, sys, pandas as pd
from confluent_kafka import Producer

broker = os.getenv("KAFKA_BROKER", "redpanda:9092")
topic  = os.getenv("KAFKA_TOPIC", "bitcoin")

csv_path = sys.argv[1] if len(sys.argv) > 1 else "/app/data/bitcoin_sample.csv"

p = Producer({"bootstrap.servers": broker})
df = pd.read_csv(csv_path)

# Wir schicken nur wenige Spalten (Datum + Close) als CSV-Zeile:
for _, row in df.iterrows():
    line = f"{row['Date']},{row['Close']}"
    p.produce(topic, value=line.encode("utf-8"))
p.flush()

print(f"Sent {len(df)} records to {topic} @ {broker}")
