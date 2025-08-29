# Data Engineering – Batch Pipeline (Kafka → Spark → Postgres)

## Architektur
- **Ingestion:** Apache Kafka (Redpanda)
- **Processing:** Apache Spark (Batch)
- **Storage:** PostgreSQL
- **Orchestrierung/IaC:** Docker Compose
- **Repro:** Git + GitHub

## Schnellstart
```bash
# 1) Services & einmalige Verarbeitung starten
docker compose up -d postgres redpanda
docker compose build producer
docker compose run --rm producer
docker compose run --rm spark

# 2) Ergebnis prüfen (Zeilen + min/max Datum)
docker exec -it postgres psql -U user -d bitcoin \
  -c "SELECT COUNT(*) AS rows, MIN(date), MAX(date) FROM daily_avg;"
