# hcoinx-driving

A driving/route intelligence module for the HCOINX platform.
Uses machine learning to predict arrival times based on distance and traffic conditions.

## Features
- Bus/vehicle arrival time prediction (Linear Regression)
- Route data ingestion from CSV
- REST API for real-time ETA queries
- Integration with HCOINX dashboard

## Usage
```bash
npm install
node server.js
```

## API
POST /predict
Body: { "distance": 5.2, "traffic": 7 }
Response: { "estimated_arrival_minutes": 19.4 }
