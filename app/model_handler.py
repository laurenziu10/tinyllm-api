import os
from openai import OpenAI
from dotenv import load_dotenv

# 🔹 Lade Umgebungsvariablen aus .env-Datei
load_dotenv()

# 🔹 Initialisiere OpenAI-Client mit API-Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔹 Erlaubte Klassifikationskategorien
VALID_CATEGORIES = ["World", "Business", "Sports", "Science/Technology"]

def classify_text(text: str) -> str:
    # Prompt für GPT
    prompt = (
        "Classify the following news article into one of the following categories:\n"
        "World, Business, Sports, Science/Technology.\n\n"
        f"Article: {text}\n"
        "Answer with one of the categories only:"
    )

    try:
        # API-Call an GPT
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
            temperature=0
        )

        # Ausgabe verarbeiten
        output = response.choices[0].message.content.strip()

        # Match gegen erlaubte Kategorien
        for category in VALID_CATEGORIES:
            if category.lower() in output.lower():
                return category

        return "Unclear"
    except Exception as e:
        return f"Error: {str(e)}"
