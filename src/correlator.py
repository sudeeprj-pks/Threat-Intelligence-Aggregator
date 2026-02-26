import ipaddress
from urllib.parse import urlparse


def is_private_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_private
    except:
        return False


def has_suspicious_tld(domain):
    suspicious_tlds = [".xyz", ".ru", ".top", ".tk", ".cn"]
    return any(domain.endswith(tld) for tld in suspicious_tlds)


def correlate_enterprise(parsed_data):

    correlation = {}

    for category, items in parsed_data.items():

        for item in items:

            if item not in correlation:
                correlation[item] = {
                    "score": 0,
                    "categories": []
                }

            correlation[item]["categories"].append(category)

            # Base scoring
            if category == "urls":
                correlation[item]["score"] += 30

            elif category == "ips":
                if is_private_ip(item):
                    correlation[item]["score"] -= 10
                else:
                    correlation[item]["score"] += 25

            elif category == "domains":
                correlation[item]["score"] += 20

    # Boost if domain appears inside URL
    for url in parsed_data["urls"]:
        domain = urlparse(url).netloc
        if domain in correlation:
            correlation[domain]["score"] += 15

    # Suspicious TLD boost
    for domain in parsed_data["domains"]:
        if has_suspicious_tld(domain):
            correlation[domain]["score"] += 10

    # Multi-category boost
    for ioc, details in correlation.items():
        if len(details["categories"]) > 1:
            correlation[ioc]["score"] += 10

    return correlation


def assign_enterprise_severity(correlation_data):

    results = {}

    for ioc, details in correlation_data.items():

        score = details["score"]

        if score >= 80:
            severity = "Critical"
        elif score >= 60:
            severity = "High"
        elif score >= 30:
            severity = "Medium"
        else:
            severity = "Low"

        confidence = max(0, min(100, score))

        results[ioc] = {
            "score": score,
            "severity": severity,
            "confidence": f"{confidence}%",
            "categories": details["categories"]
        }

    return results
