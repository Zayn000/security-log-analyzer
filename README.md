# Security Log Analyzer & Anomaly Detection Engine

A Python-based security log analysis tool designed to detect anomalous and potentially malicious behavior using statistical techniques and security-focused reasoning.

This project demonstrates practical skills in security analytics, log parsing, anomaly detection, and automation-oriented thinking.

---

## 🎯 Project Objective

Modern systems generate massive volumes of logs, making manual security monitoring inefficient and error-prone.  
This project aims to:

- Parse and normalize security-related logs
- Analyze behavioral patterns
- Detect anomalous activities that may indicate security threats
- Produce structured reports to support security decision-making

---

## 🧠 Why This Project Matters

Unlike simple log parsers, this project focuses on **security reasoning**, not just data extraction.

It simulates how a security engineer thinks:
- What is normal behavior?
- What deviation is suspicious?
- When should an alert or response be triggered?

---

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (Regex)
- Pandas & NumPy
- Basic statistical anomaly detection (Z-score / IQR)
- Structured log analysis (CSV / JSON)

---

## 📂 Project Structure


---

## 🔍 Core Features

- Log parsing using regular expressions
- Event normalization into structured formats
- Behavioral analysis per IP/user
- Statistical anomaly detection
- Classification of suspicious activities (e.g., brute-force attempts)
- JSON-based reporting for security insights
  
---

## 🔄 End-to-End Security Analysis Pipeline

This project follows a complete security analytics pipeline that mirrors real-world security operations:

1. **Log Ingestion & Parsing**
   - Raw Linux authentication logs are parsed using regular expressions.
   - Relevant security fields (timestamp, user, IP, event type) are extracted and normalized.

2. **Behavioral Analysis**
   - Authentication events are aggregated per IP address.
   - Metrics such as total events, failed logins, and successful logins are calculated.

3. **Anomaly Detection**
   - Suspicious behavior is identified based on configurable thresholds.
   - IP addresses with abnormal failed login patterns are flagged for investigation.

4. **Security Reporting**
   - Detected anomalies are exported into a structured JSON security report.
   - The report can be consumed by analysts, SOC tools, or automation workflows.

This modular design allows each stage to be extended or integrated into larger security systems.

---

## 📊 Example Security Use Case

1. A system generates Linux authentication logs.
2. The log analyzer processes the logs and detects an unusually high number of failed login attempts from a specific IP address.
3. The detection engine flags the behavior as suspicious.
4. A structured JSON report is generated, summarizing the findings and supporting further investigation or automated response.


---

## 🚧 Project Status

This project is under active development.  
Initial focus is on log parsing and anomaly detection logic, with future enhancements planned.

---

## 🔮 Future Improvements

- Support for additional log types (web, firewall, cloud)
- Threshold tuning and adaptive baselines
- Integration with alerting or response mechanisms
- Visualization of detected anomalies

---

## ⚠️ Disclaimer

This project uses **synthetic or sample log data only**.  
No real or sensitive production logs are included.

---

## 🧠 Design Decisions & Security Reasoning

- **Why threshold-based detection?**  
  Threshold-based detection provides transparency and explainability, which are critical in security operations. It allows analysts to understand *why* an alert was triggered and to tune detection logic based on the environment.

- **Why per-IP analysis?**  
  Failed authentication attempts aggregated per IP address are a common and effective indicator of brute-force or scanning behavior.

- **Why separate parser, analyzer, and detector modules?**  
  This separation follows the single-responsibility principle and reflects how real security pipelines are designed, enabling easier maintenance, testing, and future enhancements.
---

## 📐 Statistical Anomaly Detection (Z-Score)

In addition to rule-based detection, this project implements statistical anomaly detection using Z-scores.

- Failed login attempts are analyzed across all IP addresses.
- Each IP is evaluated based on how much its behavior deviates from the global mean.
- Sensitivity can be tuned via a configurable threshold.

### Calibration Example
During validation, a synthetic brute-force pattern was injected into the logs.
- At a conservative threshold (2.5), no alerts were generated.
- At a calibrated threshold (1.5), the anomalous IP was detected with a medium risk score.

This approach reduces false positives while allowing analysts to adjust detection sensitivity based on environment size and threat model.

---


## 👤 Author

Developed by a Security Automation & Detection Engineer with a focus on Python-based security analytics and automation.
