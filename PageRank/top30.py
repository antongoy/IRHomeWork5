#!/usr/bin/env python
from __future__ import print_function

import sys
import heapq

__author__ = 'anton-goy'

array = []

for line in sys.stdin:
    node, page_rank, other = line.strip('\n').split('\t')
    array.append((node, float(page_rank)))  
    
result = heapq.nlargest(30, array, key=lambda x: x[1])
print(*result, sep='\n')
