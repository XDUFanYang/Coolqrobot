# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
#from CQLog import INFO
import json

class Translate:

    def __init__(self):
      
        headers={"user-agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
        url="http://www.tianqiapi.com/api?version=v1&city="
        
  
    def getTranslate(self,word="hello"):
        data=[]
        data.append({"kw": word })
        headers={"user-agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
        try:
            r=requests.post("https://fanyi.baidu.com/sug",headers=headers,data={"kw":data[0]['kw']})
            jsonret=json.loads(r.content.decode())
            return jsonret
        except:
        	return "error"
       
        return "getTranslate Error"
        


    def fillUnivList(self,html):
        soup=BeautifulSoup(html,"html.parser")
        return soup
        #for tr in soup.find('tbody').children:
        #    if isinstance(tr,bs4.element.Tag):
        #        tds=tr('td')
        #        ulist.append([tds[0].string,tds[1].string,tds[2].string])

  