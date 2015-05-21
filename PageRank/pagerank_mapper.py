#!/usr/bin/env python
from __future__ import print_function

import sys

__author__ = 'anton-goy'

for line in sys.stdin:
    _, page_rank, out_nodes = line.strip('\n').split('\t')

    if out_nodes == '':
        continue
    else:
        out_nodes = out_nodes.split()

    page_rank = float(page_rank)
    node_degree = len(out_nodes)

    print(line.strip())

    for node in out_nodes:
        print(node, page_rank / node_degree, '', sep='\t')