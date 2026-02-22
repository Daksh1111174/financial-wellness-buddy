import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    data = pd.read_csv("data/training_data.csv")
    X = data[["income"]]
    y = data["total_expense"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "app/ml_models/expense_model.pkl")
