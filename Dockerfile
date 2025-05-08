# Schritt 1: Verwenden des offiziellen Python-Images
FROM python:3.10-slim

# Schritt 2: Arbeitsverzeichnis setzen
WORKDIR /app

# Schritt 3: Kopieren der requirements.txt und Installation der Abhängigkeiten
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Schritt 4: Kopieren des gesamten Anwendungscodes
COPY app/ /app/

# Schritt 5: Exponiere den Port 5050, der vom Flask Server verwendet wird
EXPOSE 5050

# Schritt 6: Starten der Flask-Anwendung
CMD ["python", "main.py"]
