import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from statsmodels.tsa.arima.model import ARIMA

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Financial Wellness Buddy",
    layout="wide"
)

# ----------------------------
# GLASSMORPHISM STYLE
# ----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}
.metric-card {
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}
</style>
""", unsafe_allow_html=True)

st.title("💰 Financial Wellness Buddy")

# ----------------------------
# USER INPUT
# ----------------------------
st.sidebar.header("Enter Monthly Details")

income = st.sidebar.number_input("Monthly Income", min_value=0.0, step=1000.0)

rent = st.sidebar.number_input("Rent", min_value=0.0)
food = st.sidebar.number_input("Food", min_value=0.0)
transport = st.sidebar.number_input("Transport", min_value=0.0)
entertainment = st.sidebar.number_input("Entertainment", min_value=0.0)
utilities = st.sidebar.number_input("Utilities", min_value=0.0)

# ----------------------------
# CALCULATIONS
# ----------------------------
expenses_dict = {
    "Rent": rent,
    "Food": food,
    "Transport": transport,
    "Entertainment": entertainment,
    "Utilities": utilities
}

total_expense = sum(expenses_dict.values())
savings = income - total_expense

savings_ratio = (savings / income) if income > 0 else 0

# ----------------------------
# KPI DISPLAY
# ----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("💸 Total Expense", f"₹ {total_expense:,.0f}")
col2.metric("💰 Savings", f"₹ {savings:,.0f}")
col3.metric("📊 Savings Ratio", f"{savings_ratio*100:.2f}%")

# ----------------------------
# FINANCIAL HEALTH SCORE
# ----------------------------
if income > 0:
    if savings_ratio > 0.3:
        score = 90
        status = "Excellent"
    elif savings_ratio > 0.2:
        score = 75
        status = "Good"
    elif savings_ratio > 0.1:
        score = 60
        status = "Moderate"
    else:
        score = 40
        status = "Poor"

    st.subheader("📈 Financial Health Score")
    st.progress(score)
    st.write(f"Score: **{score}/100** ({status})")

# ----------------------------
# EXPENSE BREAKDOWN (PLOTLY)
# ----------------------------
st.subheader("📊 Expense Breakdown")

if total_expense > 0:
    df = pd.DataFrame({
        "Category": list(expenses_dict.keys()),
        "Amount": list(expenses_dict.values())
    })

    fig = px.pie(
        df,
        names="Category",
        values="Amount",
        title="Expense Distribution",
        hole=0.4
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Enter expense values to display chart.")

# ----------------------------
# ARIMA FORECAST
# ----------------------------
st.subheader("📈 6-Month Expense Forecast (ARIMA)")

# Create fake historical series for demo
historical_expenses = np.array([
    total_expense * 0.9,
    total_expense * 0.95,
    total_expense,
    total_expense * 1.05,
    total_expense * 1.1
])

if total_expense > 0:

    try:
        model = ARIMA(historical_expenses, order=(1,1,1))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=6)

        forecast_df = pd.DataFrame({
            "Month": [f"Month {i+1}" for i in range(6)],
            "Forecasted Expense": forecast
        })

        fig2 = px.line(
            forecast_df,
            x="Month",
            y="Forecasted Expense",
            markers=True,
            title="Future Expense Prediction"
        )

        fig2.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )

        st.plotly_chart(fig2, use_container_width=True)

    except:
        st.error("Not enough data for forecasting.")
else:
    st.warning("Enter expense data to generate forecast.")

# ----------------------------
# INFLATION IMPACT
# ----------------------------
st.subheader("📉 Inflation Impact (6% Example)")

if total_expense > 0:
    inflation_rate = 0.06
    future_value = total_expense * ((1 + inflation_rate) ** 5)

    st.write(
        f"If inflation is 6%, your ₹{total_expense:,.0f} monthly expense "
        f"could become ₹{future_value:,.0f} in 5 years."
    )

# ----------------------------
# AI INSIGHTS
# ----------------------------
st.subheader("🤖 AI Financial Insights")

if income > 0:
    if savings_ratio < 0.1:
        st.error("Your savings rate is very low. Reduce discretionary spending.")
    elif savings_ratio < 0.2:
        st.warning("Try increasing savings by 10% to improve financial health.")
    else:
        st.success("Great savings habit! Consider investing in SIPs or Index Funds.")

