import joblib
import json
import re
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

# Load model and vectorizer
model = joblib.load("best_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Load aspect keywords
with open("aspects.json", "r") as f:
    aspects = json.load(f)

analyzer = SentimentIntensityAnalyzer()

# Clean for model
def clean_text(text):
    return re.sub(r"[^\w\s]", "", text.lower())

# Predict overall sentiment
def predict_overall_sentiment(text):
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    pred = model.predict(vectorized)[0]
    return "Positive" if pred == 1 else "Negative"

# ABSA using VADER
def analyze_aspects_vader(text):
    aspect_sentiments = {}
    sentences = sent_tokenize(text)

    for sentence in sentences:
        # Split sentence by 'but', 'and', etc.
        clauses = re.split(r'\bbut\b|\band\b|\bor\b|,', sentence)

        for clause in clauses:
            score = analyzer.polarity_scores(clause)['compound']
            cleaned_clause = clean_text(clause)

            for aspect, keywords in aspects.items():
                if any(k in cleaned_clause for k in keywords):
                    label = "Positive" if score > 0.1 else "Negative" if score < -0.1 else "Neutral"
                    aspect_sentiments[aspect] = label

    return aspect_sentiments


# Combined report
if __name__ == "__main__":
    review = input("Enter a review:\n> ")
    
    overall = predict_overall_sentiment(review)
    aspects = analyze_aspects_vader(review)

    print(f"\nOverall Sentiment: {overall}")
    print("\nAspect-Based Sentiment:")
    for asp, sent in aspects.items():
        print(f"• {asp.title()}: {sent}")
