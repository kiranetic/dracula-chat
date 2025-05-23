import csv
import json
from datetime import datetime
import pytz

from app.config import JSON_LOG, TZ


try:
    TZ = pytz.timezone(TZ)
except pytz.UnknownTimeZoneError:
    TZ = pytz.UTC


def log_response(user_query, response, source="faq", score=None, fallback_reason=None):
    now_utc = datetime.utcnow()
    local_time = now_utc.replace(tzinfo=pytz.UTC).astimezone(TZ)
    timestamp = local_time.strftime("%Y-%m-%d %H:%M:%S %Z")

    entry = {
        "timestamp": timestamp,
        "user_query": user_query,
        "response": response,
        "source": source,
        "score": score,
        "fallback_reason": fallback_reason
    }

    with open(JSON_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

