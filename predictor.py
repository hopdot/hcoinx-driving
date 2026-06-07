#!/usr/bin/env python3
"""
hcoinx-driving Bus Arrival Time Predictor
Linear regression model trained on 500 historical bus routes
Generated: 2026-06-07T07:03:02.803717
R² Score: 0.9260
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class BusPredictor:
    def __init__(self):
        # Model coefficients (auto-generated on 2026-06-07 07:03)
        self.intercept = 2.0389
        self.coefficients = {
            'distance': 3.2954,
            'traffic': 0.5032,
            'time_of_day': 0.0589,
            'day_of_week': -0.9176,
        }

    def predict(self, distance, traffic, time_of_day, day_of_week):
        """
        Predict bus arrival time in minutes.
        
        Args:
            distance (float): Distance in km
            traffic (int): Traffic level 1-10
            time_of_day (int): Hour 0-23
            day_of_week (int): Day 0-6 (Mon-Sun)
        
        Returns:
            float: Estimated arrival time in minutes
        """
        result = (self.intercept +
                  self.coefficients['distance'] * distance +
                  self.coefficients['traffic'] * traffic +
                  self.coefficients['time_of_day'] * time_of_day +
                  self.coefficients['day_of_week'] * day_of_week)
        return max(1.0, round(result, 1))

if __name__ == "__main__":
    predictor = BusPredictor()
    # Example: 5km distance, traffic level 7, 8am, Monday
    eta = predictor.predict(5.0, 7, 8, 0)
    print(f"Example prediction: 5km, traffic 7, 8am Monday = {eta} minutes")
