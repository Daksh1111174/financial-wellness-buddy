from fastapi import FastAPI
from app.routes import finance_routes, forecast_routes

app = FastAPI(title="Financial Wellness Buddy API")

app.include_router(finance_routes.router)
app.include_router(forecast_routes.router)

@app.get("/")
def root():
    return {"message": "Financial Wellness Buddy API Running 🚀"}
