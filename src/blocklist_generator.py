import os

OUTPUT_FOLDER = "../output"


def ensure_output_folder():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)


def generate_ip_blocklist(ips):
    with open(os.path.join(OUTPUT_FOLDER, "ip_blocklist.txt"), "w") as f:
        for ip in sorted(ips):
            f.write(ip + "\n")


def generate_domain_blocklist(domains):
    with open(os.path.join(OUTPUT_FOLDER, "domain_blocklist.txt"), "w") as f:
        for domain in sorted(domains):
            f.write(domain + "\n")


def generate_url_blocklist(urls):
    with open(os.path.join(OUTPUT_FOLDER, "url_blocklist.txt"), "w") as f:
        for url in sorted(urls):
            f.write(url + "\n")


def generate_all_blocklists(parsed_data):
    ensure_output_folder()

    generate_ip_blocklist(parsed_data["ips"])
    generate_domain_blocklist(parsed_data["domains"])
    generate_url_blocklist(parsed_data["urls"])
