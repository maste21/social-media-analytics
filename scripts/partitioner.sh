#!/bin/bash
# Custom partitioner for user-based partitioning

while read line; do
    user_id=$(echo "$line" | cut -d'|' -f1)
    partition=$(( $(echo "$user_id" | md5sum | tr -dc '0-9' | head -c 5) % 100 ))
    echo "${partition}"
done