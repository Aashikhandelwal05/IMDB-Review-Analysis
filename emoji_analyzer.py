import re

emoji_emotions = {
    "😂": "Joy", "😢": "Sadness", "😡": "Anger", "😍": "Love",
    "🔥": "Excitement", "😭": "Sadness", "😴": "Boredom",
    "🤮": "Disgust", "😎": "Coolness", "🤔": "Confusion",
    "👍": "Approval", "👎": "Disapproval", "🥰": "Affection"
}

def extract_emojis(text):
    emoji_pattern = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)
    return emoji_pattern.findall(text)

def map_emojis_to_emotions(emojis):
    return [emoji_emotions.get(e, "Unknown") for e in emojis]
