#!/bin/bash

hadoop fs -rm -r ./graph-lenta-hits
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-file init_mapper.py init_reducer.py \
	-mapper 'init_mapper.py' \
	-reducer 'init_reducer.py' \
	-input ./graph-lenta/part-* \
	-output ./graph-lenta-hits

