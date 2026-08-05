import pandas as pd
from sklearn.linear_model import LinearRegression
import sys
import json
import os

csv_path = sys.argv[1] if len(sys.argv) > 1 else "bus_history_large.csv"
# Training source: bus_history_large.csv
# Retrained from bus_history_large.csv: 2026-08-05 07:03:14 UTC; samples=100; r_squared=0.9916; coef_distance=3.1894; coef_traffic=0.5435; intercept=-0.2305

if not os.path.exists(csv_path):
    print(json.dumps({"error": f"CSV file not found: {csv_path}"}))
    sys.exit(1)

data = pd.read_csv(csv_path)

X = data[['distance', 'traffic']]
y = data['arrival_minutes']

model = LinearRegression()
model.fit(X, y)
r_squared = model.score(X, y)

print(json.dumps({
    "status": "model trained",
    "samples": len(data),
    "training_file": os.path.basename(csv_path),
    "r_squared": round(r_squared, 4),
    "coef_distance": round(model.coef_[0], 4),
    "coef_traffic": round(model.coef_[1], 4),
    "intercept": round(model.intercept_, 4)
}))
