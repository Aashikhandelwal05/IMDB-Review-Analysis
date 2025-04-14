from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import joblib


def plot_model_accuracies(results):
    names = list(results.keys())
    scores = list(results.values())

    plt.figure(figsize=(8, 5))
    bars = plt.bar(names, scores, color='skyblue')
    plt.title("Model Accuracy Comparison")
    plt.ylabel("Accuracy")
    plt.ylim(0.8, 1.0)

    for bar, score in zip(bars, scores):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.005, f"{score:.4f}", ha='center', fontsize=10)

    plt.tight_layout()
    plt.show()

def train_and_evaluate_models(df):
    X = df['clean_text']
    y = df['label']

    vectorizer = TfidfVectorizer(max_features=5000)
    X_vec = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=200),
        "Naive Bayes": MultinomialNB(),
        "Random Forest": RandomForestClassifier(n_estimators=100),
        "SVM": LinearSVC()
    }

    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"\n {name}")
        print(f" Accuracy: {acc:.4f}")
        print(classification_report(y_test, y_pred))
        results[name] = acc

    best_model_name = max(results, key=results.get)
    best_model = models[best_model_name]

    print(f"\n Best model: {best_model_name} with accuracy {results[best_model_name]:.4f}")

    # Save model and vectorizer
    joblib.dump(best_model, "best_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")
    print(" Model and vectorizer saved!")

    plot_model_accuracies(results)


if __name__ == "__main__":
    from load_data import load_imdb_data
    from preprocess import preprocess_dataframe

    df = load_imdb_data("IMDB Dataset.csv")
    df = preprocess_dataframe(df)
    train_and_evaluate_models(df)

