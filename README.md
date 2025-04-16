#  IMDB Review Analyzer

An intelligent sentiment analysis web app that analyzes movie reviews using a multimodal approach — combining **overall sentiment**, **aspect-based sentiment analysis (ABSA)**, and **emoji-based emotion detection**.

---

##  Features

-  **Overall Sentiment Analysis**  
  Predicts whether a review is **Positive** or **Negative** using a trained machine learning model (e.g., SVM, Logistic Regression).

-  **Aspect-Based Sentiment Analysis (ABSA)**  
  Detects opinions on specific aspects like `Acting`, `Story`, `Visuals` using keyword matching and sentiment scoring (e.g., VADER).

-  **Emoji-Based Emotion Recognition**  
  Detects emojis in reviews and maps them to emotional states such as Joy, Sadness, Confusion, Boredom, etc.

-  **Natural Language Summary Generator**  
  Generates a human-readable summary of the review, covering sentiment, aspects, and emojis.

-  **Web Interface**  
  Responsive frontend built using **HTML**, **CSS**, and **JavaScript**, with a **Flask backend** for processing and prediction.

---

##  How It Works

1. **Preprocessing:**  
   Cleans review text by removing noise, HTML tags, punctuation, etc.

2. **Prediction Pipeline:**  
   - Loads a trained sentiment analysis model (`best_model.pkl`)
   - Uses a TF-IDF or count vectorizer (`vectorizer.pkl`)
   - Predicts the review's overall sentiment

3. **Aspect Analysis:**  
   Matches keywords related to `acting`, `story`, `visuals` and assigns sentiment using VADER or another rule-based system.

4. **Emoji Detection:**  
   Extracts emojis from the text and maps each to a predefined emotion.

5. **Summary Generator:**  
   Constructs a simple explanation using overall results.

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/imdb-review-analyzer.git
cd imdb-review-analyzer

### 2. Install Dependencies

```bash
pip install -r requirements.txt

### 3. Run the Flask Server
```bash
python app.py

### 4. Open the Frontend
Open index.html in your browser (/frontend/index.html or just double-click it).