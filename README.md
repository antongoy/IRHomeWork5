# IRHomeWork5

## Site: lenta.ru
*url\_extractor.py* --- mapper. Require: file urls.txt (docids and corresponding urls).

*url\_extractor\_run.sh* --- script for running mapreduce task with url_extractor.py

## PageRank:
*init\_mapper.py* --- transform graph (url\_extractor's output) into graph with pageranks.

*init\_run.sh* --- script for running mapreduce task with init\_mapper.py


*pagerank\_mapper.py and pagerank\_reducer* --- compute pagerank for lenta.ru

*pagerank\_run.sh* --- script for running pagerank task. (By default 5 iteration)


*run.sh* = init\_run.sh + pagerank_run.sh


*top30.py* --- locally compute top30. Read from stdin.
*top30.txt* --- results after 5 iterations.

## HITS:
*init\_mapper.py and init\_reducer.py* --- transform graph (url\_extractor's output) into graph with authority and hub ranks. Add inverse edges.

*init\_run.sh* --- script for running mapreduce task with init\_mapper.py and init\_reducer.py


*hits\_mapper.py and hits\_reducer* --- HITS for lenta.ru

*hitsk\_run.sh* --- script for running HITS task. (By default 5 iteration)


*run.sh* = init\_run.sh + hits_run.sh


*top30.py* --- locally compute top30. Read from stdin.

*top30.txt* --- results after 5 iterations.
