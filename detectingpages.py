# -*- coding: utf-8 -*-
"""Detectingpages.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1koKN5D9XPX31NmWYAqJTcF3dCFTWFs_W
"""

pip install wayback

pip install requests

pip install GitPython

pip install wapiti3

import git
import urllib.request
import requests
import wayback

from datetime import date
from contextlib import redirect_stdout
client = wayback.WaybackClient()
with open('KSU.txt', 'w') as f:
    with redirect_stdout(f):
               for record in client.search('https://www.ksu.edu.sa/',
                                    to_date=date(2015, 1, 1),
                                    match_type="domain",
                                    filter_field='mimetype:text/html'):
                      print(record.url)

from IPython.utils.text import Formatter
from typing import final
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
urls = set()
with open('KSU.txt', 'r') as fi:
   with open("KSU200.txt", 'w') as fo:
    for line in fi:
        url = line.strip()
        if url not in urls:
            r = requests.get(url, headers=HEADERS)
            if r.status_code == 200:
                urls.add(url)
                fo.write(url + ' ' + str(r.status_code) + '\n')

wapiti3 -u 'https://www.ksu.edu.sa'