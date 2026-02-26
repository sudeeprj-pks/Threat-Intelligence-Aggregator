from feed_loader import load_all_feeds
from ioc_parser import parse_iocs
from correlator import correlate_enterprise, assign_enterprise_severity
from blocklist_generator import generate_all_blocklists


if __name__ == "__main__":

    print("Loading feeds...")
    feeds = load_all_feeds()

    print("Parsing and validating IOCs...")
    parsed_data = parse_iocs(feeds)

    print("Generating blocklists...")
    generate_all_blocklists(parsed_data)

    print("Running Enterprise Correlation Engine...")

    correlation = correlate_enterprise(parsed_data)
    severity_results = assign_enterprise_severity(correlation)

    print("\nEnterprise IOC Correlation Results:\n")

    for ioc, details in severity_results.items():
        print(f"IOC: {ioc}")
        print(f"  Risk Score: {details['score']}")
        print(f"  Severity: {details['severity']}")
        print(f"  Confidence: {details['confidence']}")
        print(f"  Categories: {details['categories']}")
        print("-" * 50)

    print("\n✅ Enterprise correlation completed successfully")
    print("✅ Blocklists generated inside /output folder")
