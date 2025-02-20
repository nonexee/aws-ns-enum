#!/usr/bin/env python3
import json
import ipaddress
import urllib.request

def main():
    url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
    print(f"Fetching AWS IP ranges from {url} ...")
    with urllib.request.urlopen(url) as response:
        data = json.load(response)

    # Filter for prefixes where service == "ROUTE53"
    route53_prefixes = [
        item["ip_prefix"]
        for item in data.get("prefixes", [])
        if item.get("service") == "ROUTE53"
    ]
    
    print("Found the following Route53 prefixes:")
    for prefix in route53_prefixes:
        print("  ", prefix)

    # Enumerate all IP addresses from each prefix
    ips = []
    for prefix in route53_prefixes:
        network = ipaddress.ip_network(prefix)
        ips.extend(str(ip) for ip in network)
    
    # Write IPs to file
    output_file = "aws_route53_ips.txt"
    with open(output_file, "w") as f:
        for ip in ips:
            f.write(ip + "\n")
    
    print(f"Generated {len(ips)} IPs from Route53 ranges and wrote them to {output_file}")

if __name__ == "__main__":
    main()
