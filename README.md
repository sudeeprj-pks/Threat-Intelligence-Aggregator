#  Threat Intelligence Aggregator (Non-AI)

##  Project Overview

This project implements a Threat Intelligence Aggregator designed to collect, parse, normalize, correlate, and generate blocklists from multi-source IOC feeds without using Artificial Intelligence or Machine Learning.

The system processes CSV, TXT, and JSON feeds and produces actionable intelligence outputs for defensive security controls.

---

##  Key Features

- Multi-format IOC feed ingestion
- IP, Domain, and URL validation
- Duplicate removal & normalization
- Enterprise-level risk scoring
- Severity classification (Low / Medium / High / Critical)
- Automated blocklist generation
- Deployment-ready output files

---

##  Workflow Architecture


Load Feeds
↓
Parse & Validate IOCs
↓
Normalize Data
↓
Enterprise Correlation Engine
↓
Assign Risk Score & Severity
↓
Generate Blocklists
↓
Export Results


---

##  Project Structure


Threat-Intelligence-Aggregator
├── feeds
├── src
├── output
├── screenshots
└── README.md


---

## Project Demonstration

###  Project Structure
![Project Structure](screenshots/project_structure.png)

###  Sample IOC Feeds
![Sample Feeds](screenshots/sample_feeds.png)

###  IOC Parsing & Validation
![Parsing Output](screenshots/ioc_parsing_output.png)

###  Enterprise Correlation Engine
![Correlation](screenshots/enterprise_correlation.png)

###  Generated Blocklists
![Blocklist](screenshots/blocklist_generation.png)

---

## 🛠 Technologies Used

- Python 3.13
- re (Regular Expressions)
- json
- csv
- ipaddress
- urllib.parse
- VS Code
- Windows PowerShell

---

##  Learning Outcomes

- Threat Intelligence ingestion workflows
- IOC validation & normalization
- Cross-feed correlation techniques
- Risk scoring & severity assignment
- Blue Team automation
- Blocklist-based defensive security

---

##  Future Enhancements

- STIX/TAXII feed integration
- GeoIP enrichment
- ASN lookup
- MITRE ATT&CK tagging
- Time-based risk decay
- REST API support

---

##  Author

Sudeep R J  
Cyber Security | SOC Analyst | Threat Intelligence Enthusiast
