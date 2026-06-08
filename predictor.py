import numpy as np
import pandas as pd

# hcoinx-driving Bus Arrival Predictor
# Trained on 500 route samples
# Model performance: R² = 0.9260, RMSE = 5.21 min

MODEL_COEFFICIENTS = {
    'intercept': 2.0389,
    'distance': 3.2954,
    'traffic': 0.5032,
    'time_of_day': 0.0589,
    'day_of_week': -0.9176,
}

def predict_eta(distance, traffic, time_of_day, day_of_week):
    """Predict bus arrival time in minutes."""
    eta = (
        MODEL_COEFFICIENTS['intercept'] +
        MODEL_COEFFICIENTS['distance'] * distance +
        MODEL_COEFFICIENTS['traffic'] * traffic +
        MODEL_COEFFICIENTS['time_of_day'] * time_of_day +
        MODEL_COEFFICIENTS['day_of_week'] * day_of_week
    )
    return max(1.0, round(eta, 1))

if __name__ == '__main__':
    # Example: 5km, traffic 7, 8am, Sunday
    eta = predict_eta(5.0, 7, 8, 0)
    print(f"Predicted ETA: {eta} minutes")
