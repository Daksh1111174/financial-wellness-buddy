def calculate_health_score(data):
    income = data["income"]
    total_expense = sum(data["expenses"].values())

    savings_ratio = (income - total_expense) / income

    if savings_ratio > 0.3:
        return 90
    elif savings_ratio > 0.2:
        return 75
    elif savings_ratio > 0.1:
        return 60
    else:
        return 40
