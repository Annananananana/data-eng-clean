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

  ## 📂 Daten

Dieses Repository enthält aus Platzgründen **nicht den vollständigen historischen Datensatz**, sondern nur eine kleine Beispieldatei:


- Die Datei `bitcoin_sample.csv` ist ausreichend, um den ETL-Workflow und die Architektur zu demonstrieren.  
- Die vollständige CSV `bitcoin_2017_to_2023.csv` wurde bewusst nicht ins Repository aufgenommen, da sie die GitHub-Grenze von 100 MB überschreitet.  
- Falls Sie den gesamten Datensatz nutzen möchten, laden Sie ihn bitte manuell herunter und legen Sie ihn im Ordner `data/` ab.

👉 Quelle der Rohdaten: [Kaggle – Bitcoin Historical Data (2017–2023)](https://www.kaggle.com/datasets/jkraak/bitcoin-price-dataset?resource=download)  
*(Bitte beachten: exakter Link je nach Kaggle-Dataset, hier ggf. anpassen!)*

Die `.gitignore`-Konfiguration stellt sicher, dass große Rohdaten nicht ins Repo gelangen.

