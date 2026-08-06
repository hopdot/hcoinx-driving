"""
hcoinx-driving: Bus Arrival Predictor
Trained on 100 records | R² = 0.9916
Last retrain: 2026-08-06T07:03:38.411409+00:00
"""

class BusPredictor:
    def __init__(self):
        self.intercept = -0.2305
        self.coef = {
            'distance': 3.1894,
            'traffic': 0.5435,
        }
        self.r2_score = 0.9916

    def predict(self, distance, traffic):
        """Estimate ETA in minutes."""
        result = (
            self.intercept +
            self.coef['distance'] * distance +
            self.coef['traffic'] * traffic
        )
        return max(1.0, round(result, 1))

if __name__ == "__main__":
    predictor = BusPredictor()
    eta = predictor.predict(distance=5.0, traffic=8)
    print(f"Sample prediction: {eta} minutes")
    print(f"Model R²: {predictor.r2_score}")
