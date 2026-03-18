import pandas as pd
import os

def recommend_songs(emotion):
    # Get the directory where songs.csv is located (one level up from this file)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "..", "songs.csv")
    df = pd.read_csv(csv_path)
    return df[df['mood'] == emotion].head(5)