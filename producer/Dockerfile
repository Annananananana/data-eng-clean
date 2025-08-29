FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir confluent-kafka==2.5.3 pandas==2.2.2
COPY producer.py .
ENTRYPOINT ["python", "producer.py"]
