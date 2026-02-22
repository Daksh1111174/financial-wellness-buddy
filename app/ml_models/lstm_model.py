import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_lstm_model(n_steps):
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(n_steps,1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model
