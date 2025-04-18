# src/actions/actions_mapper.py
#!/usr/bin/env python3

import sys
from common.utils import parse_line

for line in sys.stdin:
    try:
        parts = parse_line(line)
        if not parts or len(parts) != 5:
            continue
            
        _, user_id, action_type, _, _ = parts
        if action_type in ['post', 'like', 'comment', 'share']:
            # Emit composite key: user|action
            print(f"{user_id}|{action_type}\t1")
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)

