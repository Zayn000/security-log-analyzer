import pandas as pd


def detect_suspicious_ips(
    summary_df: pd.DataFrame,
    failed_login_threshold: int = 5
) -> pd.DataFrame:
    """
    Detect suspicious IP addresses based on failed login behavior.

    Flags IPs with failed logins above a defined threshold.
    """
    df = summary_df.copy()

    df["suspicious"] = df["failed_logins"] >= failed_login_threshold

    return df[df["suspicious"]].reset_index(drop=True)
