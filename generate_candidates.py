#!/usr/bin/env python3
"""
This script generates potential AWS nameserver hostnames based on a pattern:
    ns-<server_num>.awsdns-<pool_num>.<tld>
and writes them to aws_candidates.txt.
"""

import itertools

# Configuration: adjust these ranges as needed.
SERVER_NUM_START = 1
SERVER_NUM_END = 10000    # Generates ns-1 ... ns-6000
POOL_NUM_START = 1
POOL_NUM_END = 101        # Generates awsdns-1 ... awsdns-20
TLDs = ["org", "com", "net", "co.uk"]

output_file = "aws_candidates.txt"

with open(output_file, "w") as f:
    for server, pool, tld in itertools.product(range(SERVER_NUM_START, SERVER_NUM_END),
                                                 range(POOL_NUM_START, POOL_NUM_END),
                                                 TLDs):
        hostname = f"ns-{server}.awsdns-{pool}.{tld}"
        f.write(hostname + "\n")
