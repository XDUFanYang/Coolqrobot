# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
#from CQLog import INFO


class Weather:
   
    response = {}
    IdArray = []

    def __init__(self):
      
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 \
            Safari/537.36'}
        url="http://www.tianqiapi.com/api?version=v1&city="
        

    def getHTMLText(self):
        try:
            r=requests.get(url,timeout=30)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            return r.text
        except:
            return "getHTMLText error"


    def fillUnivList(self,html):
        soup=BeautifulSoup(html,"html.parser")
        return soup
        #for tr in soup.find('tbody').children:
        #    if isinstance(tr,bs4.element.Tag):
        #        tds=tr('td')
        #        ulist.append([tds[0].string,tds[1].string,tds[2].string])

  