# src/threshold/threshold_mapper.py
#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        parts = line.strip().split('\t')
        if len(parts) != 5:
            continue
            
        _, _, action_type, content_id, _ = parts
        if action_type in ['like', 'share']:
            weight = 2 if action_type == 'share' else 1
            print(f"{content_id}\t{weight}")
    except:
        pass