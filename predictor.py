"""
hcoinx-driving: Arrival Time Predictor
Supports basic and extended features (time of day, day of week)
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import json, sys, os

csv_path = sys.argv[1] if len(sys.argv) > 1 else "bus_history_large.csv"

if not os.path.exists(csv_path):
    print(json.dumps({"error": f"File not found: {csv_path}"}))
    sys.exit(1)

data = pd.read_csv(csv_path)

# Use extended features if available
if 'time_of_day' in data.columns and 'day_of_week' in data.columns:
    features = ['distance', 'traffic', 'time_of_day', 'day_of_week']
else:
    features = ['distance', 'traffic']

X = data[features]
y = data['arrival_minutes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = round(r2_score(y_test, y_pred), 4)
mae = round(mean_absolute_error(y_test, y_pred), 4)

result = {
    "status": "model trained",
    "samples": len(data),
    "features": features,
    "r2_score": r2,
    "mae_minutes": mae,
    "coefficients": {f: round(c, 4) for f, c in zip(features, model.coef_)},
    "intercept": round(model.intercept_, 4)
}

# Example predictions
examples = [
    {"distance": 2.0, "traffic": 3, "time_of_day": 9, "day_of_week": 1},
    {"distance": 5.0, "traffic": 7, "time_of_day": 8, "day_of_week": 0},
    {"distance": 10.0, "traffic": 9, "time_of_day": 18, "day_of_week": 2},
]

predictions = []
for ex in examples:
    vals = [ex[f] for f in features]
    pred = round(model.predict([vals])[0], 1)
    ex["predicted_arrival_minutes"] = pred
    predictions.append(ex)

result["example_predictions"] = predictions
print(json.dumps(result, indent=2))
