#!/bin/bash
# Calculate trending threshold using 95th percentile

INPUT=$1
OUTPUT=$2

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input $INPUT \
    -output $OUTPUT \
    -mapper "python3 src/threshold/threshold_mapper.py" \
    -reducer "python3 src/threshold/threshold_reducer.py" \
    -file src/threshold/threshold_mapper.py \
    -file src/threshold/threshold_reducer.py

# Store threshold in HDFS
hadoop fs -cat ${OUTPUT}/part-00000 | grep THRESHOLD > config/threshold.txt
hadoop fs -put -f config/threshold.txt /config/