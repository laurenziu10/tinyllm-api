# 🧠 AG News Textklassifikation mit OpenAI

Dieses Projekt stellt eine REST-API bereit, die Nachrichtenartikel aus dem **AG News Dataset** mit Hilfe der **OpenAI API (GPT-3.5)** automatisch in vier Kategorien klassifiziert:

- 🌍 World
- 🏦 Business
- ⚽ Sports
- 🧪 Science/Technology

Zusätzlich enthält das Projekt eine benutzerfreundliche **GUI** zur direkten Klassifikation im Browser.

---

## 🚀 Features

- ✅ REST-API mit Flask
- ✅ OpenAI GPT-3.5 Klassifikation
- ✅ GUI (HTML/JS) mit AG News Random Sample & Live-Feedback
- ✅ Evaluation-Skript mit AG News Testdaten
- ✅ Docker-Container & GitHub Actions CI/CD Pipeline

---

## 📁 Projektstruktur

```
tinyllm-api/
├── app/
│   ├── main.py               # Flask-API mit /predict, /random, /gui, /
│   ├── model_handler.py      # OpenAI-Klassifikation
│   ├── test_with_dataset.py  # Evaluation mit AG News
│   ├── gui.html              # Interaktive Klassifikations-GUI
│   └── index.html            # Landing Page
├── requirements.txt
├── Dockerfile
├── VERSION
├── .env                      # Enthält OPENAI_API_KEY (nicht committen!)
└── .github/workflows/
    └── docker-build.yml      # CI/CD Pipeline für Build & Test
```

---

## 🧪 Endpunkte der REST-API

| Route         | Beschreibung                             |
|---------------|-------------------------------------------|
| `/predict`    | POST: JSON mit `{ "text": "..." }` → Klassifikation |
| `/random`     | GET: Zufälliger AG News Artikel aus Testdaten |
| `/gui`        | Interaktive Web-GUI im ChatGPT-Stil       |
| `/`           | Landing Page mit Button zur GUI           |

---

## 🐳 Docker

### Build & Run lokal

```bash
docker build -t textclassifier-openai:$(cat VERSION) .
docker run -p 5050:5050 -e OPENAI_API_KEY=sk-... textclassifier-openai:$(cat VERSION)
```

Dann öffnen: [http://localhost:5050/gui](http://localhost:5050/gui)

---

## 🔁 Evaluation mit AG News Testdaten

```bash
docker run --rm -e OPENAI_API_KEY=sk-... textclassifier-openai:$(cat VERSION) python test_with_dataset.py
```

---

## 🧪 GitHub Actions (CI/CD)

Bei jedem Push auf `main` wird automatisch:

1. Die Version gelesen (`VERSION`)
2. Das Docker-Image gebaut
3. `test_with_dataset.py` im Container ausgeführt

Datei: `.github/workflows/docker-build.yml`

---

## 🛠️ Lokales Setup (nur bei Entwicklung)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
python app/main.py
```

.env Datei:

```
OPENAI_API_KEY=sk-...
```

---

## 🧾 Lizenz

MIT License – frei nutzbar mit Quellverweis.

---

## 👨‍💻 Autor

Erstellt von [Laurenziu B.] im Rahmen einer Übungsaufgabe zu LLM-gestützter Textklassifikation.
