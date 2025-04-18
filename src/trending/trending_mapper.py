# src/trending/trending_mapper.py
#!/usr/bin/env python3

import sys
from common.utils import load_hot_content
import random

hot_content = load_hot_content()

for line in sys.stdin:
    try:
        parts = line.strip().split('\t')
        if len(parts) != 5:
            continue
            
        _, _, action_type, content_id, _ = parts
        if action_type in ['like', 'share']:
            # Handle data skew using salting
            if content_id in hot_content:
                salt = random.randint(1, 10)
                content_id = f"{content_id}_{salt}"
            
            weight = 2 if action_type == 'share' else 1
            print(f"{content_id}\t{weight}")
    except:
        pass
