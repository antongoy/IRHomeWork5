#!/usr/bin/env python
from __future__ import print_function

import sys

__author__ = 'anton-goy'

current_node = None
current_out_nodes = []
current_in_nodes = []
current_authority = 0
current_hub = 0

for line in sys.stdin:
    node, line_type, unknown1, unknown2 = line.strip('\n').split('\t')

    if not current_node:
        current_node = node

    if current_node != node:
        print(current_node, current_authority, current_hub, sep='\t', end='\t')
        print(current_out_nodes, end='\t')
        print(current_in_nodes)

        current_node = node
        current_out_nodes = []
        current_in_nodes = []
        current_authority = 0
        current_hub = 0

    line_type = int(line_type)

    if line_type == 0:
        current_out_nodes = unknown1
        current_in_nodes = unknown2
    else:
        current_authority += int(unknown1)
        current_hub += int(unknown2)

print(current_node, current_authority, current_hub, sep='\t', end='\t')
print(current_out_nodes, end='\t')
print(current_in_nodes)