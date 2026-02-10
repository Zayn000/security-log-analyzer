from src.parser import parse_auth_log
from src.analyzer import analyze_auth_activity
from src.detector import detect_suspicious_ips
from src.utils import export_security_report

df = parse_auth_log("logs/sample_auth.log")
summary = analyze_auth_activity(df)
suspicious = detect_suspicious_ips(summary)

export_security_report(
    suspicious,
    "output/security_report.json"
)

print("Security report generated.")
