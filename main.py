from load_data import load_imdb_data
from preprocess import preprocess_dataframe
from train_models import train_and_evaluate_models

# Step 1: Load
df = load_imdb_data("IMDB Dataset.csv")

# Step 2: Preprocess
df = preprocess_dataframe(df)

# Step 3: Train & Evaluate
train_and_evaluate_models(df)
