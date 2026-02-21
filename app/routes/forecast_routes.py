from fastapi import APIRouter
from app.ml_models.arima_model import arima_forecast

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.post("/arima")
def forecast(data: dict):
    expenses = data["expenses"]
    prediction = arima_forecast(expenses)
    return {"forecast": prediction.tolist()}
