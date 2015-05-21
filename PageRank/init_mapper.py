#!/usr/bin/env python
from __future__ import print_function

import sys

__author__ = 'anton-goy'


def main():
    for line in sys.stdin:
        node, out_nodes = line.strip('\n').split('\t')
        print(node, 0.15, out_nodes, sep='\t')

if __name__ == '__main__':
    main()
