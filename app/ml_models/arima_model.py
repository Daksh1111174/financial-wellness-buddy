from statsmodels.tsa.arima.model import ARIMA
import numpy as np

def arima_forecast(expense_list):
    series = np.array(expense_list)
    model = ARIMA(series, order=(2,1,2))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=6)
    return forecast
  
