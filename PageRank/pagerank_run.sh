#!/bin/bash

hadoop fs -rm -r ./graph-lenta-pagerank/output 
hadoop fs -mv ./graph-lenta-pagerank/part-* ./graph-lenta-pagerank/input.txt

for (( i=1; i <= 5; i++))
do 
	hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
		-file pagerank_mapper.py pagerank_reducer.py \
		-mapper 'pagerank_mapper.py' \
		-reducer 'pagerank_reducer.py' \
		-input ./graph-lenta-pagerank/input.txt \
		-output ./graph-lenta-pagerank/output/

	hadoop fs -rm -skipTrash ./graph-lenta-pagerank/input.txt
	hadoop fs -mv ./graph-lenta-pagerank/output/part-* ./graph-lenta-pagerank/input.txt
	hadoop fs -rm -r -skipTrash ./graph-lenta-pagerank/output
done


