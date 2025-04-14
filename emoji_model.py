# emoji_model.py

emoji_sentiment_map = {
    "😊": 1, "😂": 1, "😍": 1, "😁": 1,
    "😢": -1, "😡": -1, "🤬": -1, "😠": -1,
    "😐": 0, "😶": 0,
    # Add more as needed
}

def analyze_emoji_sentiment(emoji_string):
    if not emoji_string:
        return 0  # Neutral if no emojis

    score = 0
    for em in emoji_string:
        score += emoji_sentiment_map.get(em, 0)
    return score / len(emoji_string)  # Normalize
