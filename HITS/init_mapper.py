#!/usr/bin/env python
from __future__ import print_function

import sys

__author__ = 'anton-goy'

for line in sys.stdin:
    node, out_nodes = line.strip('\n').split('\t')
    print(node, 0, out_nodes, sep='\t')

    out_nodes = out_nodes.split()

    for n in out_nodes:
        print(n, 1, node, sep='\t')
