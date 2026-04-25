from datetime import datetime

date = "2025-01-01T00:00:00Z"
datetime.fromisoformat(date.replace("Z", "+00:00"))
