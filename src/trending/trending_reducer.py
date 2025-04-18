# src/trending/trending_reducer.py
#!/usr/bin/env python3

import sys
from common.utils import log_error

threshold = None

def load_threshold():
    try:
        with open('threshold.txt', 'r') as f:
            for line in f:
                if line.startswith('THRESHOLD'):
                    return float(line.strip().split('\t')[1])
    except:
        log_error("Threshold file not found")
        sys.exit(1)

threshold = load_threshold()

for line in sys.stdin:
    try:
        content_id, scores = line.strip().split('\t', 1)
        total = sum(int(score) for score in scores.split('\t'))
        
        if total >= threshold:
            print(f"{content_id}\t{total}")
    except Exception as e:
        log_error(str(e))