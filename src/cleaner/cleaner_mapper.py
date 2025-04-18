#!/usr/bin/env python3

import sys
import json
from datetime import datetime

def is_valid_timestamp(ts):
    try:
        datetime.fromisoformat(ts.replace('Z', '+00:00'))
        return True
    except:
        return False

def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except:
        return False

counters = {
    'valid': 0,
    'invalid_ts': 0,
    'invalid_json': 0,
    'malformed': 0
}

for line in sys.stdin:
    line = line.strip()
    try:
        parts = line.split('\t')
        if len(parts) != 5:
            counters['malformed'] += 1
            continue
        
        ts, uid, action, cid, meta = parts
        
        if not is_valid_timestamp(ts):
            counters['invalid_ts'] += 1
            continue
            
        if not is_valid_json(meta):
            counters['invalid_json'] += 1
            continue
            
        counters['valid'] += 1
        print(line)
        
    except:
        counters['malformed'] += 1

for k,v in counters.items():
    print(f'COUNTER|{k}|{v}', file=sys.stderr)