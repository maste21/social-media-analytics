#!/usr/bin/env python3

import sys
from collections import defaultdict

# Initialize counters
counters = defaultdict(int)

def log_counters():
    for counter, value in counters.items():
        print(f"COUNTER|{counter}|{value}", file=sys.stderr)

for line in sys.stdin:
    try:
        # Simply pass through cleaned records
        print(line.strip())
        counters['valid_output'] += 1
        
    except Exception as e:
        counters['reducer_errors'] += 1
        print(f"ERROR|cleaner_reducer|{str(e)}", file=sys.stderr)
        continue

# Log final counters
log_counters()