# -*- coding: utf-8 -*-
import pypinyin
from bs4 import BeautifulSoup
import requests
import re
#from CQLog import INFO


class Search:
   

    def __init__(self):
      
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 \
            Safari/537.36'}
        self.url="https://www.tianqi.com/"
        self.target=''
        self.html=''
    
    def invert(self,word):
        s = ''
        for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
            s += ''.join(i)
        self.target=s
        self.url=self.url+self.target+'/15'
        return self.url

    def getHTMLText(self):
        try:
            r=requests.get(self.url,timeout=30,headers=self.header)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            self.html=r.text
            return 'getHTMLText finished'
        except:
            return "getHTMLText error"


    def fillUnivList(self):
        soup=BeautifulSoup(self.html,"html.parser")
        #get_text()太爽 直接下一级的tag过滤
        w=[]
        for it in soup.find_all('div',attrs={'class':"table_day tbg"}):
            date=it('em')[0].string
            content=it.find('li',attrs={'class':"temp"})
            forecast=content.get_text()
            w.append({date:forecast})
        return w


        #for tr in soup.find('tbody').children:
        #    if isinstance(tr,bs4.element.Tag):
        #        tds=tr('td')
        #        ulist.append([tds[0].string,tds[1].string,tds[2].string])

  