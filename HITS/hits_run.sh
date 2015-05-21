#!/bin/bash

hadoop fs -rm -r ./graph-lenta-hits/output 
hadoop fs -mv ./graph-lenta-hits/part-* ./graph-lenta-hits/input.txt

for (( i=1; i <= 5; i++))
do 
	hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-file hits_mapper.py hits_reducer.py \
		-mapper 'hits_mapper.py' \
		-reducer 'hits_reducer.py' \
		-input ./graph-lenta-hits/input.txt \
		-output ./graph-lenta-hits/output/

	hadoop fs -rm -skipTrash ./graph-lenta-hits/input.txt
	hadoop fs -mv ./graph-lenta-hits/output/part-* ./graph-lenta-hits/input.txt
	hadoop fs -rm -r -skipTrash ./graph-lenta-hits/output
done
