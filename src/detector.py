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


def detect_suspicious_ips_zscore(df: pd.DataFrame, threshold: float = 2.5):
    """
    Detect suspicious IPs using Z-score anomaly detection.
    """
    mean_failed = df["failed_logins"].mean()
    std_failed = df["failed_logins"].std()

    if std_failed == 0:
        df["z_score"] = 0
    else:
        df["z_score"] = (df["failed_logins"] - mean_failed) / std_failed

    suspicious = df[df["z_score"] >= threshold].copy()
    suspicious["risk_level"] = suspicious["z_score"].apply(
        lambda z: "high" if z >= 3 else "medium"
    )

    return suspicious

