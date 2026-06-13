"""
hcoinx-driving: Bus Arrival Predictor
Trained on 100 records | R² = 0.9916
Last retrain: 2026-06-13T07:02:42.787461
"""

import numpy as np

class BusPredictor:
    def __init__(self):
        self.intercept = -0.1294
        self.coef = {
            'distance': 3.1920,
            'traffic': 0.5431,
            'time_of_day': -0.0087,
            'day_of_week': -0.0046,
        }
        self.r2_score = 0.9916

    def predict(self, distance, traffic, time_of_day, day_of_week):
        """Estimate ETA in minutes."""
        result = (
            self.intercept +
            self.coef['distance'] * distance +
            self.coef['traffic'] * traffic +
            self.coef['time_of_day'] * time_of_day +
            self.coef['day_of_week'] * day_of_week
        )
        return max(1.0, round(result, 1))

# Example usage
if __name__ == "__main__":
    predictor = BusPredictor()
    
    # Test: 5km, heavy traffic (8/10), morning (8am), weekday (1=Monday)
    eta = predictor.predict(distance=5.0, traffic=8, time_of_day=8, day_of_week=1)
    print(f"Sample prediction: {eta} minutes")
    print(f"Model R²: {predictor.r2_score}")
