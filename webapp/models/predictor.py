import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model(df):
    """Train a Random Forest model to predict sales conversion."""
    X = df.drop(columns=['ProdTaken', 'CustomerID'])
    y = df['ProdTaken']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    with open("models/sales_model.pkl", "wb") as f:
        pickle.dump(model, f)

    return model
