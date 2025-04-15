
import joblib
import re
import string
import emoji

# Load saved model and vectorizer
model = joblib.load("best_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Emoji sentiment mapping
emoji_sentiment_map = {
    "😊": 1, "😂": 1, "😍": 1, "😁": 1, "😃": 1, "😄": 1,
    "😢": -1, "😡": -1, "🤬": -1, "😠": -1, "😞": -1, "😭": -1,
    "😐": 0, "😶": 0
}

# Extract emojis
def extract_emojis(text):
    return ''.join(ch for ch in text if ch in emoji.EMOJI_DATA)

# Score emojis
def analyze_emoji_sentiment(emoji_string):
    if not emoji_string:
        return 0  # Neutral
    score = 0
    for em in emoji_string:
        score += emoji_sentiment_map.get(em, 0)
    return score / len(emoji_string)  # Normalize

# Text cleaning
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

# Predict function
def predict_sentiment(text):
    # Step 1: Text prediction
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    text_prediction = model.predict(vectorized)[0]  # 0 or 1

    # Step 2: Emoji prediction
    emojis = extract_emojis(text)
    emoji_score = analyze_emoji_sentiment(emojis)

    # Step 3: Combine
    if emoji_score > 0.2:
        final_prediction = 1
    elif emoji_score < -0.2:
        final_prediction = 0
    else:
        final_prediction = text_prediction

    print(f"\nInput: {text}")
    print(f"Text-Based Sentiment: {'Positive' if text_prediction == 1 else 'Negative'}")
    print(f"Emoji Emotion : {'Positive' if emoji_score > 0 else 'Negative' if emoji_score < 0 else 'Neutral'}")
    print(f"Final Sentiment: {'Positive' if final_prediction == 1 else 'Negative'}")
def predict_sentiment(text, return_label=False):
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    label = "Positive" if prediction == 1 else "Negative"
    if return_label:
        return label
    print(f"\nInput: {text}")
    print(f"Predicted Sentiment: {label}")

# Run with user input
if __name__ == "__main__":
    while True:
        user_input = input("\nEnter a sentence to analyze sentiment (or type 'exit' to quit):\n> ")
        if user_input.lower() == 'exit':
            break
        predict_sentiment(user_input)
