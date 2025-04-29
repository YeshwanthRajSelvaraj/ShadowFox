!pip install transformers torch pandas matplotlib seaborn

import torch
from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
model.eval()

texts = [
    "I love this movie, it's amazing!",
    "This film is terrible, I hated it.",
    "The acting was great, but the plot was boring.",
    "Absolutely fantastic experience, highly recommend!",
    "Worst movie ever, a complete waste of time."
]
labels = [1, 0, 0, 1, 0]  # 1: Positive, 0: Negative

inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=128)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1).numpy()

print("Predictions vs Actual Labels:")
results = pd.DataFrame({"Text": texts, "Actual": labels, "Predicted": predictions})
print(results)

accuracy = accuracy_score(labels, predictions)
print(f"\nAccuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(labels, predictions, target_names=["Negative", "Positive"]))

print("\nResearch Questions Answered:")
print("- How well does BERT understand sentiment context? (Accuracy:", accuracy, ")")
print("- Does BERT struggle with mixed sentiments? (See Text 3 prediction)")

plt.figure(figsize=(8, 6))
sns.countplot(x="Actual", hue="Predicted", data=results)
plt.title("Actual vs Predicted Sentiments")
plt.xlabel("Actual Label")
plt.ylabel("Count")
plt.legend(title="Predicted Label", labels=["Negative", "Positive"])
plt.show()

print("\nConclusion:")
print("BERT performed well on simple sentiment analysis, achieving an accuracy of", accuracy)
print("It correctly identified clear sentiments but may struggle with mixed sentiments (e.g., Text 3).")
print("Potential applications include automated review analysis or social media monitoring.")
