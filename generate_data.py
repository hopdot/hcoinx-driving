"""
hcoinx-driving: Synthetic route data generator
Generates realistic bus/vehicle arrival data for model training
"""
import csv, random, math

random.seed(2026)

rows = [['distance', 'traffic', 'time_of_day', 'day_of_week', 'arrival_minutes']]

for _ in range(500):
    distance = round(random.uniform(0.5, 20.0), 2)
    traffic = random.randint(1, 10)
    time_of_day = random.randint(0, 23)  # hour
    day_of_week = random.randint(0, 6)   # 0=Mon

    # Rush hour multiplier
    rush = 1.3 if time_of_day in [7, 8, 9, 17, 18, 19] else 1.0
    weekend = 0.85 if day_of_week in [5, 6] else 1.0

    arrival = round(
        distance * 3.2 * rush * weekend +
        traffic * 0.5 +
        random.gauss(0, 1.5),
        1
    )
    arrival = max(1.0, arrival)
    rows.append([distance, traffic, time_of_day, day_of_week, arrival])

with open('bus_history_large.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Generated {len(rows)-1} rows -> bus_history_large.csv")
