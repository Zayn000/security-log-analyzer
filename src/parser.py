import re
import pandas as pd
from datetime import datetime


FAILED_PATTERN = re.compile(
    r"(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+).*Failed password for (invalid user )?(?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

SUCCESS_PATTERN = re.compile(
    r"(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+).*Accepted password for (?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)


def parse_auth_log(file_path: str) -> pd.DataFrame:
    """
    Parse Linux authentication logs and return a structured DataFrame.

    Columns:
    - timestamp
    - username
    - ip
    - event_type
    - raw_message
    """
    records = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            failed_match = FAILED_PATTERN.search(line)
            success_match = SUCCESS_PATTERN.search(line)

            if failed_match:
                records.append({
                    "timestamp": failed_match.group("timestamp"),
                    "username": failed_match.group("user"),
                    "ip": failed_match.group("ip"),
                    "event_type": "FAILED_LOGIN",
                    "raw_message": line
                })

            elif success_match:
                records.append({
                    "timestamp": success_match.group("timestamp"),
                    "username": success_match.group("user"),
                    "ip": success_match.group("ip"),
                    "event_type": "SUCCESS_LOGIN",
                    "raw_message": line
                })

    return pd.DataFrame(records)
