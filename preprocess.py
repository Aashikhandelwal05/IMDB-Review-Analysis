import re
import nltk
from nltk.corpus import stopwords
import emoji


def extract_emojis(text):
    return ''.join(ch for ch in text if ch in emoji.EMOJI_DATA)

# Download stopwords oncepip 
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize and remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

def preprocess_dataframe(df):
    df['clean_text'] = df['review'].apply(clean_text)
    df['label'] = df['sentiment'].map({'positive': 1, 'negative': 0})
    return df


