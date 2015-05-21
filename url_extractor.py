#!/usr/bin/env python
from __future__ import print_function

import re
import sys

__author__ = 'anton-goy'

from lxml.html import document_fromstring

from urlparse import urlparse

from base64 import b64decode
from zlib import decompress


def main():
    urls = {}

    for line in open('urls.txt'):
        doc_id, url = line.strip().split('\t')
        doc_id = int(doc_id)

        if not url.endswith('/'):
            url += '/'

        parse_url = urlparse(url)

        if parse_url.netloc == 'lenta.ru':
            urls[doc_id] = parse_url.path + ('?' + parse_url.query if parse_url.query else '')

    for line in sys.stdin:
        doc_id, document = line.strip().split('\t')
        doc_id = int(doc_id)

        document = decompress(b64decode(document))
 	document = document_fromstring(document)

        links = set()

        regexp1 = 'http://lenta.ru'
        regexp2 = 'lenta.ru'
        regexp3 = '/'

        for anchor_elem in document.xpath('.//a[@href]'):
            url = anchor_elem.attrib['href'].strip()

            if url.startswith(regexp1) or url.startswith(regexp2) or url.startswith(regexp3):
		if not url.endswith('/'):
			url += '/'

                parse_url = urlparse(url)
                link = parse_url.path if parse_url.path else '/' + \
                                                             ('?' + parse_url.query if parse_url.query else '')
                if not link in links:
                    links.add(link.encode('utf-8'))

        if doc_id in urls:
            print(urls[doc_id], end='\t')
            print(*sorted(list(links)))


if __name__ == '__main__':
    main()
