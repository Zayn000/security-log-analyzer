import pandas as pd


def analyze_auth_activity(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze authentication activity and produce aggregated metrics per IP.

    Returns a DataFrame with:
    - ip
    - total_events
    - failed_logins
    - success_logins
    """
    df = df.copy()

    df["failed"] = df["event_type"] == "FAILED_LOGIN"
    df["success"] = df["event_type"] == "SUCCESS_LOGIN"

    summary = (
        df.groupby("ip")
        .agg(
            total_events=("event_type", "count"),
            failed_logins=("failed", "sum"),
            success_logins=("success", "sum"),
        )
        .reset_index()
    )

    return summary
