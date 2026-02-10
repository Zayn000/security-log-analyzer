from src.parser import parse_auth_log
from src.analyzer import analyze_auth_activity

df = parse_auth_log("logs/sample_auth.log")
summary = analyze_auth_activity(df)

print(summary)
