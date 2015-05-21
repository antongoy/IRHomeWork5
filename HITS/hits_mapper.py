#!/usr/bin/env python
from __future__ import print_function

import sys

__author__ = 'anton-goy'


for line in sys.stdin:
    node, authority, hub, out_nodes, in_nodes = line.strip('\n').split('\t')
    print(node, 0, out_nodes, in_nodes, sep='\t')

    out_nodes = out_nodes.split()
    in_nodes = in_nodes.split()

    for node in out_nodes:
        print(node, 1, int(authority), 0, sep='\t')

    for node in in_nodes:
        print(node, 1, 0, int(hub), sep='\t')