# Dockerfile

FROM python:3.10-slim

WORKDIR /app

# Requirements im Root
COPY requirements.txt .

# App-Quellcode
COPY app/ /app/

# Umgebungsvariablen (optional – besser mit -e Flag übergeben)
COPY .env .env

# Installiere Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5050

CMD ["python", "main.py"]
