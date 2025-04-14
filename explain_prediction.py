import joblib
import re
import string
from lime.lime_text import LimeTextExplainer
import numpy as np

# Load model & vectorizer
model = joblib.load("best_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Define class names
class_names = ['Negative', 'Positive']

# Text cleaning (same as your clean_text)
def clean_text(text):
    text = text.lower()
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.strip()

# Wrapper for prediction probability (needed by LIME)
def predict_proba(texts):
    cleaned = [clean_text(t) for t in texts]
    vec = vectorizer.transform(cleaned)
    return model.predict_proba(vec)

# Explain a single prediction
def explain(text):
    explainer = LimeTextExplainer(class_names=class_names)
    explanation = explainer.explain_instance(text, predict_proba, num_features=10)
    
    import webbrowser
    import os
    html_path = "lime_explanation.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(explanation.as_html())

    webbrowser.open("file://" + os.path.abspath(html_path))



# Run
if __name__ == "__main__":
    review = input("Enter a review to explain:\n> ")
    explain(review)
