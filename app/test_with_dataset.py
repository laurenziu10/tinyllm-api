# Evaluation-Skript: Nutzt echte AG News Testdaten
from datasets import load_dataset
from model_handler import classify_text

dataset = load_dataset("ag_news", split="test[:10]")  # kleine Stichprobe

id2label = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Science/Technology"
}

correct = 0
total = 0

for item in dataset:
    text = item["text"]
    true_label = id2label[item["label"]]
    pred_label = classify_text(text)

    print(f"\nText: {text}")
    print(f"Prediction: {pred_label} | Ground Truth: {true_label}")

    if pred_label.lower() == true_label.lower():
        correct += 1
    total += 1

print(f"\nAccuracy on sample: {correct}/{total} = {correct/total:.2f}")
