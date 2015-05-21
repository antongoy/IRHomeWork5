#!/usr/bin/env python
from __future__ import print_function

import sys

__author__ = 'anton-goy'

current_node = None
current_out_nodes = []
current_in_nodes = []

for line in sys.stdin:
    node, line_type, unknown = line.strip('\n').split('\t')

    if not current_node:
        current_node = node

    if current_node != node:
        print(current_node, 1, 1, end='\t', sep='\t')
        print('' if not current_out_nodes else current_out_nodes, end='\t')
        print(*current_in_nodes)

        current_node = node
        current_out_nodes = []
        current_in_nodes = []

    line_type = int(line_type)

    if line_type == 0:
        current_out_nodes = unknown
    else:
        current_in_nodes.append(unknown)

print(current_node, 1, 1, end='\t', sep='\t')
print('' if not current_out_nodes else current_out_nodes, end='\t')
print(*current_in_nodes)