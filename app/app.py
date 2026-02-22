import streamlit as st
import pandas as pd
import numpy as np
import joblib
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

st.set_page_config(page_title="Financial Wellness Buddy", layout="wide")

st.title("💰 Financial Wellness Buddy")

# ---- USER INPUT ----
income = st.number_input("Enter Monthly Income", min_value=0)

rent = st.number_input("Rent")
food = st.number_input("Food")
transport = st.number_input("Transport")
entertainment = st.number_input("Entertainment")

total_expense = rent + food + transport + entertainment
savings = income - total_expense

# ---- DISPLAY KPIs ----
col1, col2, col3 = st.columns(3)

col1.metric("Total Expense", total_expense)
col2.metric("Savings", savings)
col3.metric("Savings Ratio", f"{round((savings/income)*100 if income>0 else 0,2)}%")

# ---- HEALTH SCORE ----
if income > 0:
    savings_ratio = savings/income
    if savings_ratio > 0.3:
        score = 90
    elif savings_ratio > 0.2:
        score = 75
    elif savings_ratio > 0.1:
        score = 60
    else:
        score = 40

    st.subheader("📊 Financial Health Score")
    st.progress(score)
    st.write(f"Score: {score}/100")

# ---- CATEGORY PIE CHART ----
data = pd.DataFrame({
    "Category": ["Rent", "Food", "Transport", "Entertainment"],
    "Amount": [rent, food, transport, entertainment]
})

fig, ax = plt.subplots()
ax.pie(data["Amount"], labels=data["Category"], autopct='%1.1f%%')
st.pyplot(fig)

# ---- ARIMA FORECAST ----
st.subheader("📈 6 Month Expense Forecast (ARIMA)")

expense_series = np.array([rent, food, transport, entertainment, total_expense])

if len(expense_series) > 3:
    model = ARIMA(expense_series, order=(1,1,1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=6)

    st.line_chart(forecast)
