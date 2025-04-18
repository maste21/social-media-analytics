#!/usr/bin/env python3

import sys
import json
from collections import defaultdict

current_user = None
action_counts = defaultdict(int)

def emit_sorted_actions(user, counts):
    # Separate posts from other actions for priority sorting
    post_count = counts.get('post', 0)
    sorted_actions = []
    
    # First add posts if present
    if post_count > 0:
        sorted_actions.append(('post', post_count))
    
    # Sort other actions by count descending, then alphabetically
    other_actions = [(k,v) for k,v in counts.items() if k != 'post']
    sorted_others = sorted(other_actions, 
                         key=lambda x: (-x[1], x[0]))
    
    # Combine results
    final_sorted = sorted_actions + sorted_others
    
    # Output as JSON string
    print(f"{user}\t{json.dumps(final_sorted)}")

for line in sys.stdin:
    try:
        # Input format: user|action<TAB>count
        key, count = line.strip().split('\t', 1)
        user, action = key.split('|', 1)
        count = int(count)
        
        if user != current_user:
            if current_user:
                emit_sorted_actions(current_user, action_counts)
            current_user = user
            action_counts = defaultdict(int)
        
        action_counts[action] += count
        
    except Exception as e:
        print(f"ERROR|actions_reducer|{str(e)}", file=sys.stderr)
        continue

# Process last user
if current_user:
    emit_sorted_actions(current_user, action_counts)