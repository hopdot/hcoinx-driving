"""
hcoinx-driving: Bus Arrival Predictor
Trained on 500 records | R² = 0.9171
Last retrain: 2026-11-21T07:07:03.909152+00:00
"""

class BusPredictor:
    def __init__(self):
        self.intercept = -0.1064
        self.coef = {
            'distance': 3.3017,
            'traffic': 0.5087,
        }
        self.r2_score = 0.9171

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
