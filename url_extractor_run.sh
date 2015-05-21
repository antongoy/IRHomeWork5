#!/bin/bash

hadoop fs -rm -r ./graph-lenta
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-numReduceTasks 1 \
	-file url_extractor.py urls.txt \
	-mapper 'url_extractor.py' \
	-reducer org.apache.hadoop.mapred.lib.IdentityReducer \
	-input /data/sites/lenta.ru/all/docs-*.txt \
	-output graph-lenta
