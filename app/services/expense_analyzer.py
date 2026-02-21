def analyze_expense(data):
    income = data["income"]
    expenses = sum(data["expenses"].values())

    savings = income - expenses
    savings_ratio = savings / income

    return {
        "total_expense": expenses,
        "savings": savings,
        "savings_ratio": round(savings_ratio, 2)
    }
  
