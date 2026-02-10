from src.parser import parse_auth_log
from src.analyzer import analyze_auth_activity
from src.detector import detect_suspicious_ips

df = parse_auth_log("logs/sample_auth.log")
summary = analyze_auth_activity(df)
suspicious = detect_suspicious_ips(summary)

print(suspicious)
