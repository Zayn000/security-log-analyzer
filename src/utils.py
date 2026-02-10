import json
from datetime import datetime
import pandas as pd


def export_security_report(df: pd.DataFrame, output_path: str):
    """
    Export detected suspicious activity to a JSON security report.
    """
    report = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "total_suspicious_ips": len(df),
        "findings": df.to_dict(orient="records")
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
