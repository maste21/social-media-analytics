# src/join/join_reducer.py
#!/usr/bin/env python3

import sys
import json
from common.utils import log_error

current_user = None
profile_data = None
activities = []

def emit_joined():
    if profile_data and activities:
        try:
            clean_activities = [json.loads(a) for a in activities]
            print(f"{current_user}\t{profile_data}\t{json.dumps(clean_activities)}")
        except:
            log_error(f"Invalid JSON for user {current_user}")

for line in sys.stdin:
    try:
        user_id, data_type, data = line.strip().split('\t', 2)
        
        if user_id != current_user:
            if current_user:
                emit_joined()
            current_user = user_id
            profile_data = None
            activities = []
        
        if data_type == 'profile':
            profile_data = data
        elif data_type == 'activity':
            activities.append(data)
            
    except Exception as e:
        log_error(f"Join reducer error: {str(e)}")

if current_user:
    emit_joined()