import ipaddress
from urllib.parse import urlparse
import re


def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def extract_domain_from_url(url):
    parsed = urlparse(url)
    return parsed.netloc


def is_ip_format(value):
    pattern = r"^\d+\.\d+\.\d+\.\d+$"
    return re.match(pattern, value)


def parse_iocs(feed_data):
    parsed_data = {
        "ips": set(),
        "domains": set(),
        "urls": set()
    }

    for feed_name, items in feed_data.items():
        for item in items:
            item = item.strip()

            if validate_ip(item):
                parsed_data["ips"].add(item)

            elif item.startswith("http"):
                parsed_data["urls"].add(item)
                domain = extract_domain_from_url(item)
                parsed_data["domains"].add(domain)

            elif is_ip_format(item):
                continue  # Skip invalid IP-like strings

            else:
                parsed_data["domains"].add(item)

    return parsed_data
