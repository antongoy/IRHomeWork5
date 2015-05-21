#!/usr/bin/env python
from __future__ import print_function

import sys
import heapq

__author__ = 'anton-goy'

array = []

for line in sys.stdin:
    node, auth, hub, _, _ = line.strip('\n').split('\t')
    array.append((node, int(auth), int(hub)))  
    
top_auths = heapq.nlargest(30, array, key=lambda x: x[1])
top_hubs = heapq.nlargest(30, array, key=lambda x: x[2])

print('Top authorities:')
print(*top_auths, sep='\n')

print('\nTop hubs:')
print(*top_hubs, sep='\n')
