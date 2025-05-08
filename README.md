# 🧠 AG News Textklassifikation mit OpenAI API

Dieses Projekt implementiert eine REST-API zur Klassifikation von Nachrichtentexten basierend auf dem **AG News Dataset**. Die Klassifikation erfolgt wahlweise mit einem lokalen LLM oder – wie in dieser Umsetzung – mit der **OpenAI API** (`gpt-3.5-turbo`).

---

## 🚀 Features

- Klassifikation in 4 Kategorien:
  - 🌍 World
  - 🏦 Business
  - 🧪 Science/Technology
  - ⚽ Sports
- OpenAI-gestütztes Modell (ChatGPT)
- REST-API via Flask (`/predict`)
- Docker-ready ✅
- `.env`-basiertes API-Key-Handling 🔐
- Integrierter AG News Evaluation-Test
- CI-ready für GitHub Actions

---

## 📦 Projektstruktur

```
tinyllm-api/
├── app/
│   ├── main.py               ← Flask REST-API
│   ├── model_handler.py      ← OpenAI-Anbindung
│   ├── test_with_dataset.py ← Evaluation mit AG News
│   └── requirements.txt
├── .env                      ← OpenAI API Key
├── Dockerfile
└── README.md
```

---

## 🛠️ Setup

### 🔹 Lokale Installation

```bash
git clone https://github.com/dein-benutzername/tinyllm-api.git
cd tinyllm-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
```

### 🔹 `.env` Datei erstellen

```env
OPENAI_API_KEY=sk-...
```

---

## 🧪 API testen

### ▶️ Starten

```bash
python app/main.py
```

### 🔄 Request

```bash
curl -X POST http://localhost:5050/predict   -H "Content-Type: application/json"   -d '{"text": "Apple releases a new AI chip for MacBooks."}'
```

### 🔁 Beispielantwort

```json
{
  "category": "Science/Technology",
  "input": "Apple releases a new AI chip for MacBooks."
}
```

---

## 📊 AG News Test

```bash
python app/test_with_dataset.py
```

Gibt 5–10 Beispielartikel aus dem AG News Testset aus und vergleicht Klassifikation mit Ground Truth. (Accuracy ~90 % mit GPT-3.5)

---

## 🐳 Docker

### 🔹 Build

```bash
docker build -t textclassifier-openai .
```

### 🔹 Run

```bash
docker run -p 5050:5050 -e OPENAI_API_KEY=sk-... textclassifier-openai
```

---

## 🧪 GitHub Actions (optional)

`.github/workflows/docker-build.yml`:

```yaml
name: Docker Build

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - run: docker build -t textclassifier-openai .
```

---

## 📚 Quellen

- [AG News Dataset (Huggingface)](https://huggingface.co/datasets/ag_news)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Flask](https://flask.palletsprojects.com/)

---

## 🧾 Lizenz

MIT License – frei nutzbar mit Angabe.

---

## ✨ Autor

> Erstellt von [Laurenziu B.] – im Rahmen einer Übungsaufgabe zur LLM-gestützten Textklassifikation mit Python, Flask und OpenAI.