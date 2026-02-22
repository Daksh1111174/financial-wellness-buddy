import joblib

def predict_expense(income):
    model = joblib.load("app/ml_models/expense_model.pkl")
    return model.predict([[income]])[0]
