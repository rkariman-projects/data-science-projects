import pandas as pd
import os

def load_weather_data():
    """
    Load the weather dataset from weather_eda/data folder.
    """
    base_dir = os.path.dirname(os.path.dirname(os.getcwd()))
    data_path = os.path.join(base_dir, "weather_eda", "data", "weatherHistory.csv")
    
    df = pd.read_csv(data_path)
    print("✅ Dataset Loaded Successfully!")
    print("📊 Shape:", df.shape)
    print("\n📋 Columns:\n", df.columns)
    return df
