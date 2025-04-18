# src/threshold/threshold_reducer.py
#!/usr/bin/env python3

import sys
import numpy as np

scores = []
for line in sys.stdin:
    try:
        content_id, score = line.strip().split('\t')
        scores.append(int(score))
    except:
        pass

if scores:
    threshold = np.percentile(scores, 95)
    print(f"THRESHOLD\t{threshold}")