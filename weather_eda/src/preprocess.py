import pandas as pd
import numpy as np

def clean_and_engineer(df):
    """
    Clean missing values, parse dates, and add engineered features.
    """
    # Drop missing
    df = df.dropna(subset=["Temperature (C)", "Apparent Temperature (C)", "Humidity"])

    # Date features
    df["Formatted Date"] = pd.to_datetime(df["Formatted Date"], utc=True)
    df["Year"] = df["Formatted Date"].dt.year
    df["Month"] = df["Formatted Date"].dt.month
    df["Hour"] = df["Formatted Date"].dt.hour

    # Feature Engineering
    df["Temp_Diff"] = df["Apparent Temperature (C)"] - df["Temperature (C)"]
    df["is_Rainy"] = df["Summary"].str.contains("Rain", case=False, na=False).astype(int)

    # Outlier detection
    Q1 = df["Temperature (C)"].quantile(0.25)
    Q3 = df["Temperature (C)"].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df["Temperature (C)"] < (Q1 - 1.5 * IQR)) | (df["Temperature (C)"] > (Q3 + 1.5 * IQR))]

    print(f"⚠️ Outliers Detected: {len(outliers)} ({len(outliers)/len(df)*100:.2f}%)")

    return df
