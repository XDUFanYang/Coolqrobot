#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:qdf time:2019/1/21

from lxml import etree
import requests
from bs4 import BeautifulSoup
import requests

url = "https://www.zhihu.com/hot"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 \
            Safari/537.36'}

url = "https://www.zhihu.com/hot"
try:
    r=requests.get(url,timeout=30,headers=headers)

    r.raise_for_status()
    r.encoding=r.apparent_encoding
    html=r.text
except:
    print("error")


soup=BeautifulSoup(html,"html.parser")
# print(html)
w=[]
for it in soup.find_all('div',attrs={'class':"HotItem-index"}):
    content=it.find('h2',attrs={'class':"HotItem-title"})
    print(content.get_text())

