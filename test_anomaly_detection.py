import unittest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from anomaly_detection import detect_trend_anomalies, check_new_value_by_trend, generate_anomaly_report

class TestTrendAnomalyDetection(unittest.TestCase):

    def setUp(self):
        # Create a dummy trend dataset
        base_date = datetime(2025, 4, 1)
        self.df = pd.DataFrame({
            'business_date': [base_date + timedelta(days=i) for i in range(20)],
            'row_count': [1000 + i * 50 for i in range(20)]  # linear increasing trend
        })

    def test_detects_no_anomaly_on_linear_trend(self):
        result = detect_trend_anomalies(self.df, window=5, deviation_threshold=3.0)
        self.assertFalse(result['is_anomaly'].any(), "Should not detect anomalies in a clean linear trend")

    def test_detects_anomaly_on_spike(self):
        df = self.df.copy()
        df.at[15, 'row_count'] += 1000  # big spike
        result = detect_trend_anomalies(df, window=5, deviation_threshold=3.0)
        self.assertTrue(result.at[15, 'is_anomaly'], "Should detect spike as anomaly")

    def test_check_new_value_by_trend_detects_outlier(self):
        recent_data = self.df.copy()
        new_val = 5000  # extreme outlier
        is_anomaly = check_new_value_by_trend(new_val, recent_data, window=5, threshold=3.0)
        self.assertTrue(is_anomaly, "Should detect extreme value as anomaly")

    def test_generate_report_contains_latest_status(self):
        df = self.df.copy()
        df.at[19, 'row_count'] += 1000  # last value is anomaly
        result = detect_trend_anomalies(df, window=5, deviation_threshold=3.0)
        report = generate_anomaly_report(result, window=5, threshold=3.0)
        self.assertIn("Latest date", report)
        self.assertIn("Anomaly Detected", report, "Latest anomaly should be reported")

    def test_generate_report_with_no_anomalies(self):
        result = detect_trend_anomalies(self.df, window=5, deviation_threshold=3.0)
        report = generate_anomaly_report(result, window=5, threshold=3.0)
        self.assertIn("No anomalies detected", report)

if __name__ == '__main__':
    unittest.main()
