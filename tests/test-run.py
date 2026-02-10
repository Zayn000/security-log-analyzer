from src.parser import parse_auth_log
from src.analyzer import analyze_auth_activity
from src.detector import detect_suspicious_ips_zscore
from src.utils import export_security_report

# 1. Parse and analyze logs
df = parse_auth_log("logs/sample_auth.log")
summary = analyze_auth_activity(df)

# 2. Map 'failed_logins' to 'failed_attempts' to match the detector function's requirement
# This ensures compatibility without modifying the original function logic
if 'failed_logins' in summary.columns:
    summary['failed_attempts'] = summary['failed_logins']

# 3. Execute anomaly detection using Z-score
suspicious = detect_suspicious_ips_zscore(summary)

# 4. Export the findings to a JSON file
export_security_report(
    suspicious,
    "output/security_report.json"
)

print("Security report generated successfully.")
