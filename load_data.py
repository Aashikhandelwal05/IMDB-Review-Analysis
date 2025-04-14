import pandas as pd

def load_imdb_data(path="IMDB Dataset.csv"):
    df = pd.read_csv(path)
    print(" Dataset loaded. Shape:", df.shape)
    print("Label distribution:\n", df['sentiment'].value_counts())
    return df

# Optional test run
if __name__ == "__main__":
    df = load_imdb_data()
    print(df.head())

