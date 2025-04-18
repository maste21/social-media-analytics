#!/bin/bash

# Initialize environment
source config/cluster.properties

# Clean previous output
hadoop fs -rm -r /output/*

# Run data cleaning
echo "=== Phase 1: Data Cleaning ==="
hadoop jar $HADOOP_STREAMING \
    -D mapreduce.job.name="SocialMedia_Cleaning" \
    -input /input/social_media_logs.txt \
    -output /output/cleaned \
    -mapper "python3 src/cleaner/cleaner_mapper.py" \
    -reducer "python3 src/cleaner/cleaner_reducer.py" \
    -file src/cleaner/cleaner_mapper.py \
    -file src/cleaner/cleaner_reducer.py

# Calculate trending threshold
echo "=== Phase 2: Threshold Calculation ==="
./scripts/threshold_calculator.sh /output/cleaned /output/threshold

# Process user actions
echo "=== Phase 3: Action Processing ==="
hadoop jar $HADOOP_STREAMING \
    -D mapreduce.job.name="SocialMedia_Actions" \
    -D stream.num.map.output.key.fields=2 \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
    -input /output/cleaned \
    -output /output/actions \
    -mapper "python3 src/actions/actions_mapper.py" \
    -reducer "python3 src/actions/actions_reducer.py" \
    -file src/actions/actions_mapper.py \
    -file src/actions/actions_reducer.py

# Identify trending content
echo "=== Phase 4: Trending Identification ==="
hadoop jar $HADOOP_STREAMING \
    -D mapreduce.job.name="SocialMedia_Trending" \
    -cacheFile /config/threshold.txt#threshold.txt \
    -input /output/cleaned \
    -output /output/trending \
    -mapper "python3 src/trending/trending_mapper.py" \
    -reducer "python3 src/trending/trending_reducer.py" \
    -file src/trending/trending_mapper.py \
    -file src/trending/trending_reducer.py

# Join with user profiles
echo "=== Phase 5: Data Join ==="
hadoop jar $HADOOP_STREAMING \
    -D mapreduce.job.name="SocialMedia_Join" \
    -D mapreduce.reduce.memory.mb=12288 \
    -input /output/actions \
    -input /input/user_profiles.txt \
    -output /output/final \
    -mapper "python3 src/join/join_mapper.py" \
    -reducer "python3 src/join/join_reducer.py" \
    -file src/join/join_mapper.py \
    -file src/join/join_reducer.py

echo "=== Pipeline Complete ==="