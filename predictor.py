"""hcoinx-driving: Bus Arrival Time Predictor
Generated: 2026-06-10T07:02:38.240187
R² Score: 0.9260
RMSE: 5.21 minutes
"""

import numpy as np

MODEL = {
    "intercept": 2.0389,
    "coefficients": {
        "distance": 3.2954,
        "traffic": 0.5032,
        "time_of_day": 0.0589,
        "day_of_week": -0.9176,
    },
    "r2_score": 0.9260,
    "rmse_minutes": 5.21,
}

def predict(distance, traffic, time_of_day, day_of_week):
    """Predict arrival time in minutes."""
    intercept = MODEL["intercept"]
    c = MODEL["coefficients"]
    result = (
        intercept +
        c["distance"] * distance +
        c["traffic"] * traffic +
        c["time_of_day"] * time_of_day +
        c["day_of_week"] * day_of_week
    )
    return max(1.0, round(result * 10) / 10)

if __name__ == "__main__":
    # Test prediction
    test_result = predict(5.0, 7, 8, 0)  # 5km, traffic 7, 8am, Monday
    print(f"Test: 5km + traffic 7 @ 8am Monday -> {test_result} minutes")
    print(f"Model stats: R²={MODEL['r2_score']:.4f}, RMSE={MODEL['rmse_minutes']:.2f}min")
