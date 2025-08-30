# Implementierung & Reflexion (Phase 2)

## Umsetzung des Projekts
Das Projekt wurde als **Microservice-Architektur mit Docker Compose** umgesetzt.  
Die drei zentralen Komponenten sind:
- **PostgreSQL** als persistente Datenbank
- **Redpanda (Kafka)** für Event Streaming
- **Apache Spark** für ETL-Verarbeitung und Aggregationen  

Die Container wurden in einem lokalen Docker-Netzwerk orchestriert.  
Ein **Producer-Service** lädt Beispieldaten (`bitcoin_sample.csv`) und streamt diese in Kafka.  
Spark konsumiert die Daten, berechnet Tagesdurchschnitte und schreibt die Ergebnisse in die Datenbank.

---

## Orientierung an Zielen / Ressourcen
- Ziel: Aufbau einer skalierbaren, wartbaren Datenpipeline im lokalen Umfeld.  
- Umsetzung mit minimalen Ressourcen (lokaler Laptop, Docker-Container).  
- Große CSV-Dateien (>100 MB) wurden **nicht ins Git übernommen**. Stattdessen verweist das Repo auf die Rohdatenquelle (Kaggle).  

---

## Probleme & Risiken
- **Große Datenmengen**: GitHub erlaubt keine Dateien >100 MB → Lösung: `.gitignore` + Verweis auf externe Datenquelle.  
- **Abhängigkeiten in Spark**: Für Kafka-Integration mussten zusätzliche Pakete geladen werden.  
- **Datenkonsistenz**: Duplicate-Key-Fehler in PostgreSQL traten auf, wenn Spark-Jobs mehrfach gestartet wurden.  
  - Lösung: Anpassung der Inserts (Upsert/Truncate vor Neuimport wäre denkbar).  

---

## Status & Fortschritt
- Alle Services laufen lokal zuverlässig in Docker.  
- Datenfluss funktioniert: CSV → Producer → Kafka → Spark → PostgreSQL.  
- Ergebnisse sind in der Tabelle `daily_avg` einsehbar.  
- Projektziele (Reliability, Scalability, Maintainability) wurden eingehalten.  
- [ETL Pipeline Screenshot](docs/images/ETL-Pipeline_Screenshot.png)


---

**Hinweis:** Zusätzlich zum ursprünglichen Konzept wurde in der Umsetzung **Redpanda** (Kafka-kompatibel) sowie ein kleiner **Python Producer** verwendet.  
Dies war notwendig, um die ETL-Pipeline mit Streaming-Daten zu versorgen und die Kommunikation mit Spark lokal zu validieren, auch wenn dieser Aspekt im ursprünglichen Konzept nicht explizit enthalten war.

---

## Screenshot (Beispiel Docker Setup / Spark Job)
👉 Hier Screenshot einfügen (`/docs/images/etl_pipeline.png` oder direkt aus VS Code/PebblePad):

---

## Fazit
Die Microservice-Architektur erfüllt die Anforderungen der Aufgabenstellung.  
Sie ist modular, erweiterbar und kann bei Bedarf in eine Cloud-Umgebung übertragen werden.  
Besonders herausfordernd war das Handling von externen Datenquellen und die Integration von Spark mit Kafka.  
Durch die iterative Umsetzung konnte ein lauffähiges und dokumentiertes System erfolgreich aufgebaut werden.
