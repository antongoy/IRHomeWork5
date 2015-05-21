#!/bin/sh

hadoop fs -rm -r ./graph-lenta-pagerank
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-numReduceTasks 1 \
	-file init_mapper.py \
	-mapper 'init_mapper.py' \
	-reducer org.apache.hadoop.mapred.lib.IdentityReducer \
	-input ./graph-lenta/part-* \
	-output ./graph-lenta-pagerank			
