# src/join/join_mapper.py
#!/usr/bin/env python3

import sys
import os
from common.utils import parse_line

def is_profile_file():
    return 'user_profiles.txt' in os.environ.get('mapreduce_map_input_file', '')

for line in sys.stdin:
    try:
        if is_profile_file():
            # Profile data: user_id\tname\tlocation\tjoined_date
            parts = parse_line(line)
            if parts and len(parts) >= 4:
                print(f"{parts[0]}\tprofile\t{','.join(parts[1:])}")
        else:
            # Activity data: user_id\tjson_actions
            parts = parse_line(line)
            if parts and len(parts) == 2:
                print(f"{parts[0]}\tactivity\t{parts[1]}")
    except Exception as e:
        pass

