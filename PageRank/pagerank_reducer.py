#!/usr/bin/env python
from __future__ import print_function

import sys

__author__ = 'anton-goy'

current_key = None
current_page_rank = 0.0
current_out_nodes = []

for line in sys.stdin:
    key, page_rank, out_nodes = line.strip('\n').split('\t')

    page_rank = float(page_rank)

    if out_nodes == '':
        out_nodes = []
    else:
        out_nodes = out_nodes.split()

    if current_key is None:
        current_key = key

    if key != current_key:
        print(current_key, 0.15 + 0.85 * current_page_rank, sep='\t', end='\t')
        print(*current_out_nodes)

        current_key = key
        current_page_rank = 0.0
        current_out_nodes = []

    if out_nodes:
        current_out_nodes = out_nodes
    else:
        current_page_rank += page_rank

print(current_key, 0.15 + 0.85 * current_page_rank, sep='\t', end='\t')
print(*current_out_nodes)
