## Anomaly Detection with Trend-Based Linear Regression (Time Series Data)

#### Objective
Develop a robust anomaly detection system that:
1. Identifies unexpected spikes/drops in time series data
2. Learns normal patterns from historical trends
3. Provides visual and statistical evidence for anomalies
4. Validates new data points against learned patterns

#### Business Use cases
1. **Financial Monitoring**: Detect unusual transactions or revenue fluctuations
2. **IT Operations**: Identify abnormal server metrics or traffic patterns  
3. **Manufacturing**: Spot defects in production line sensor data
4. **Inventory Management**: Catch unexpected changes in stock levels

#### Implementation Details/Flow
1. **Data Load and cleanup**
2. **Trend Modeling**: Fit linear regression to 7-day rolling window to compute expected value
3. **Anomaly Scoring**: Calculate deviation score: |actual - expected| / standard deviation
4. **Anomaly Flagging**: Flag anomalies if deviation score > 3.0
5. **New Data Check**: Validate new data by computing deviation score against recent trend
6. **Visualization**: Plot time series with actual values, trend, and anomaly markers in Jupyter
7. **Reporting**: Report anomalies in last 7 days and latest value status


#### Files included
- Jupyter notebook (statistical_anomaly_detection.ipynb) - Jupyter notebook for interactive code evaluation
- Sample input CSVs (trends2.csv and trends3.csv)
- Unit test cases (test_anomaly_detection.py) - Test cases for original python script evaluation and validation.