## Anomaly Detection with Rolling Z-Score (Time Series Data)

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
2. **Baseline Calculation**: Compute 7-day rolling mean/std with 5-period warmup, Fallback to expanding stats for initial periods
3. **Anomaly Scoring**: 
    - Calculate Z-scores: (current - mean) / std
    - Flag points where |Z-score| > 2.5
4. **Trend Validation**:
    - Compare with prior window's slope
    - Confirm anomalies break established patterns
5. **Visualization**: Generate time series plot with anomalies highlighted
6. **New Data Evaluation**: Recalculate window stats, Compute Z-score, Return boolean flag