# Q2: Cloud Security Evaluation

## Incident
Snowflake customer data breach (2024) — 165 customers affected via credential stuffing using stolen credentials from infostealer malware.

## Analysis Files

| File | Description |
|------|-------------|
| `incident-analysis.md` | Detailed incident summary, cloud components, shared responsibility breakdown, and prevention recommendations |

## Key Findings

- **Root Cause:** Absence of MFA on customer accounts; credential theft via infostealer malware on personal devices
- **Cloud Model:** SaaS (Snowflake data warehouse)
- **Shared Responsibility:** Customer-side identity governance failure, not provider infrastructure breach
- **Prevention:** Universal MFA, least-privilege access, anomaly detection, customer-managed encryption, credential lifecycle management
