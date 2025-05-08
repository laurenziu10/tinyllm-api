
# AG News Klassifikator mit OpenAI API und Docker

Dieses Projekt implementiert einen Textklassifikator, der mithilfe des **AG News Dataset** Nachrichtenartikel in vier Kategorien klassifiziert: **World**, **Business**, **Sports** und **Science/Technology**. Die Klassifikation erfolgt entweder durch ein **OpenAI LLM** (wie GPT-3.5) oder ein anderes Sprachmodell.

## 🚀 Features

- Textklassifikation auf Basis des **AG News Datasets**.
- Klassifikation in 4 Kategorien:
  - 🌍 World
  - 🏦 Business
  - ⚽ Sports
  - 🧪 Science/Technology
- OpenAI-gestütztes Modell (ChatGPT).
- REST API zur Klassifikation von Texten.
- GUI zur Interaktion mit dem Modell.
- Docker-Container für die Ausführung.
- GitHub Actions für Continuous Integration.

## 📦 Projektstruktur

```bash
tinyllm-api/
├── .github/
│   └── workflows/
│       └── docker-build.yml          ← GitHub Actions Workflow für Docker Build
├── app/
│   ├── main.py                       ← Flask REST API und GUI
│   ├── model_handler.py              ← OpenAI API-Integration für die Klassifikation
│   ├── test_with_dataset.py          ← Testskript, das das AG News Dataset mit dem Modell validiert
│   ├── index.html                    ← Landing Page für den Klassifikator
│   └── gui.html                      ← GUI für die Klassifikation von Texten
├── .env                              ← Umgebungsvariablen wie OpenAI API Key
├── Dockerfile                        ← Dockerfile zur Erstellung des Docker-Containers
├── requirements.txt                  ← Python-Abhängigkeiten
├── VERSION                           ← Version des Projekts
└── README.md                         ← Diese Datei
```

## 🛠️ Setup

### 1. Repository Klonen

Zuerst solltest du das Repository auf deinem lokalen Rechner klonen:

```bash
git clone https://github.com/your-username/tinyllm-api.git
cd tinyllm-api
```

### 2. Docker Installation

Stelle sicher, dass Docker auf deinem System installiert ist. Falls nicht, kannst du Docker [hier herunterladen](https://www.docker.com/get-started).

### 3. Docker-Image bauen

Baue das Docker-Image mit dem folgenden Befehl:

```bash
docker build -t textclassifier-openai .
```

Dieser Befehl lädt die notwendigen Abhängigkeiten und stellt sicher, dass die Umgebung für die Flask-Anwendung und das Modell korrekt konfiguriert ist.

### 4. Docker-Container starten

Starte den Docker-Container mit dem folgenden Befehl:

```bash
docker run -e OPENAI_API_KEY=sk-your-openai-api-key -p 5050:5050 textclassifier-openai
```

- Ersetze `sk-your-openai-api-key` durch deinen tatsächlichen OpenAI API-Key. Du kannst den Key auch sicher mit einer `.env`-Datei und der Option `--env-file` übergeben, wenn du ihn nicht direkt in der Kommandozeile angeben möchtest.

- Der Port 5050 wird vom Flask-Server verwendet. Wenn du den Port ändern möchtest, ändere die `EXPOSE`-Zeile im Dockerfile.

---

## 💻 API verwenden

Die REST API stellt einen Endpunkt `/predict` zur Verfügung, der Texte klassifiziert.

### Beispiel-Request:

```bash
curl -X POST http://localhost:5050/predict -H "Content-Type: application/json" -d '{"text": "NASA announces new mission to Mars."}'
```

### Beispiel-Antwort:

```json
{
  "category": "Science/Technology",
  "input": "NASA announces new mission to Mars."
}
```

---

## 🖥️ GUI verwenden

Die Anwendung enthält auch eine einfache GUI, die über die Route `/gui` erreichbar ist. Du kannst mit dieser GUI Texte eingeben und vorhersagen lassen.

### Um die GUI zu öffnen:

Gehe zu `http://localhost:5050/gui` in deinem Webbrowser.

---

## 🚀 Testen der AG News Klassifikation

Um die AG News Klassifikation zu testen, kannst du das Testskript ausführen. Es wird eine kleine Stichprobe des AG News Datasets geladen und die Vorhersagen des Modells mit den tatsächlichen Kategorien verglichen.

```bash
docker run --rm textclassifier-openai python app/test_with_dataset.py
```

### Beispiel-Ausgabe:

```bash
Text: Fears for T N pension after talks...
Prediction: Business | Ground Truth: Business

Text: The Race is On: Second Private Team...
Prediction: Science/Technology | Ground Truth: Science/Technology

Accuracy on sample: 9/10 = 0.90
```

---

## 📄 Erklärung der wichtigsten Dateien

### `.github/workflows/docker-build.yml`

Diese Datei enthält den **GitHub Actions Workflow**, der bei jedem Push auf den `main`-Branch ausgelöst wird. Er führt den Build-Prozess des Docker-Images aus und startet anschließend den AG News Test. Der OpenAI API-Key wird dabei sicher über **GitHub Secrets** übergeben.

### `app/main.py`

Hier wird die **Flask-Anwendung** gestartet. Sie stellt zwei Haupt-Routen zur Verfügung:
- `/predict`: Akzeptiert Text und gibt die Kategorie des Artikels zurück.
- `/random`: Gibt zufällig einen Artikel aus dem AG News Dataset zurück.

### `app/model_handler.py`

In dieser Datei wird das Modell von OpenAI integriert, um Texte zu klassifizieren. Der **API-Key** wird über die Umgebungsvariable `OPENAI_API_KEY` bereitgestellt.

### `app/test_with_dataset.py`

Das Skript lädt eine kleine Stichprobe aus dem **AG News Dataset** und testet, wie gut das Modell bei der Vorhersage der richtigen Kategorie abschneidet.

---

## 💡 Erweiterungsmöglichkeiten

- **Modellwahl**: Statt OpenAI könnte ein anderes Modell von Huggingface verwendet werden (z.B. BERT, GPT-2).
- **GUI-Erweiterung**: Eine Möglichkeit zur Anzeige der Vorhersagegenauigkeit und eine detailliertere Benutzeroberfläche.
- **Skalierung**: Derzeit läuft die Anwendung auf `localhost:5050`. Für eine echte Produktionsumgebung kann sie in einem Cloud-Service wie **AWS** oder **Heroku** bereitgestellt werden.
- **Datenbankintegration**: Speichere Klassifikationsergebnisse oder Artikel in einer Datenbank, um eine größere Datenanalyse zu ermöglichen.

---

## 🧪 CI/CD und GitHub Actions

### 1. Workflow auslösen

Der Workflow wird bei jedem **Push auf den `main`-Branch** automatisch ausgelöst. Sobald du deinen Code in den GitHub-Repository pushst, wird das Docker-Image gebaut und der Test ausgeführt.

```bash
git add .
git commit -m "Update Workflow and Dockerfile"
git push origin main
```

### 2. GitHub Actions-Logs überprüfen

Gehe auf **GitHub → Dein Repository → Actions**, um den Status des Workflows zu überprüfen.

---

## 📝 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**.

---

## ✨ Autor

> Erstellt von [Laurenziu B.] – im Rahmen eines Übungsprojekts zur Textklassifikation mit **OpenAI GPT-3**, **Flask** und **Docker**.
