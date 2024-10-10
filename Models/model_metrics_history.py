from datetime import datetime


class Model_Metrics_History:
    
    def __init__(self, model_id, accuracy, precision, recall, f1_score, top_features, timestamp,user_id):
        self.model_id = model_id
        self.accuracy = accuracy
        self.precision = precision
        self.recall = recall
        self.f1_score = f1_score
        self.top_features = top_features
        self.timestamp = timestamp
        self.user_id = user_id
        
        
    
    def get_most_recent_metric(metrics):
        # Sort by timestamp and return the most recent one
        sorted_metrics = sorted(metrics, key=lambda x: x[7], reverse=True)
        return sorted_metrics[0] if sorted_metrics else None