from src.parser import parse_auth_log
from src.analyzer import analyze_auth_activity
from src.detector import detect_suspicious_ips_zscore
from src.utils import export_security_report

df = parse_auth_log("logs/sample_auth.log")
summary = analyze_auth_activity(df)

suspicious = detect_suspicious_ips_zscore(summary)

export_security_report(
    suspicious,
    "output/security_report_zscore.json"
)

print("Z-score security report generated.")
