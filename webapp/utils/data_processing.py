import pandas as pd
from sklearn.preprocessing import LabelEncoder

def clean_data(df):
    """Handle missing values and clean dataset."""
    df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill missing numeric values with mean
    df.fillna(df.mode().iloc[0], inplace=True)  # Fill categorical missing values with mode
    return df

def encode_categorical(df):
    """Convert categorical columns to numeric using Label Encoding."""
    label_encoders = {}
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    return df, label_encoders
