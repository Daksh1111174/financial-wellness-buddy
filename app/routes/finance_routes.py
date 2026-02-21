from fastapi import APIRouter
from app.services.expense_analyzer import analyze_expense
from app.services.health_score import calculate_health_score

router = APIRouter(prefix="/finance", tags=["Finance"])

@router.post("/analyze")
def analyze(data: dict):
    result = analyze_expense(data)
    score = calculate_health_score(data)
    return {
        "analysis": result,
        "financial_health_score": score
    }
