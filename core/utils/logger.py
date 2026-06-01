import os
import json
from datetime import datetime

class DataLogger:
    """Handles system event logging for production backend utilities."""
    def __init__(self, log_dir="storage/logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def write_entry(self, level: str, message: str):
        payload = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": level.upper(),
            "message": message
        }
        target_file = os.path.join(self.log_dir, "app.log")
        
        with open(target_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload) + "\n")

if __name__ == "__main__":
    logger = DataLogger()
    logger.write_entry("INFO", "Core subsystem initialized.")
