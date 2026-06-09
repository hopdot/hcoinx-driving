#!/usr/bin/env python3
"""
hcoinx-driving: Bus/Vehicle ETA Prediction Model
Generated: 2026-06-09T07:02:29.913145
R² Score: 0.9260
RMSE: 5.21 minutes
Dataset: 500 routes
"""

import numpy as np
import pandas as pd

class BusArrivalPredictor:
    """Linear regression model for bus arrival time prediction."""
    
    def __init__(self):
        self.model_name = "hcoinx-driving v1"
        self.r2_score = 0.9260
        self.rmse = 5.21
        self.intercept = 2.0389
        self.coefficients = {
            'distance': 3.2954,
            'traffic': 0.5032,
            'time_of_day': 0.0589,
            'day_of_week': -0.9176
        }
    
    def predict(self, distance, traffic, time_of_day, day_of_week):
        """Predict arrival time in minutes."""
        result = (
            self.intercept +
            self.coefficients['distance'] * distance +
            self.coefficients['traffic'] * traffic +
            self.coefficients['time_of_day'] * time_of_day +
            self.coefficients['day_of_week'] * day_of_week
        )
        return max(1.0, round(result, 1))

if __name__ == "__main__":
    predictor = BusArrivalPredictor()
    
    # Example usage
    test_cases = [
        {"distance": 5.0, "traffic": 7, "time_of_day": 8, "day_of_week": 1},
        {"distance": 10.0, "traffic": 3, "time_of_day": 14, "day_of_week": 5},
        {"distance": 2.5, "traffic": 9, "time_of_day": 18, "day_of_week": 4},
    ]
    
    print(f"Model: {predictor.model_name}")
    print(f"R² Score: {predictor.r2_score:.4f}")
    print(f"RMSE: {predictor.rmse:.2f} minutes\n")
    
    for case in test_cases:
        eta = predictor.predict(**case)
        print(f"Distance: {case['distance']}km, Traffic: {case['traffic']}/10 → {eta} min")
