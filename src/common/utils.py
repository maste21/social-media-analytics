# src/common/utils.py
import sys
import json
import logging

logging.basicConfig(level=logging.INFO)

def log_error(message):
    logging.error(message)
    print(f"ERROR|{message}", file=sys.stderr)

def parse_line(line):
    try:
        return line.strip().split('\t')
    except:
        log_error("Malformed line encountered")
        return None

def load_hot_content():
    try:
        with open('config/hot_content.txt', 'r') as f:
            return set(line.strip() for line in f)
    except Exception as e:
        log_error(f"Error loading hot content: {str(e)}")
        return set()

def validate_json(data):
    try:
        json.loads(data)
        return True
    except:
        return False