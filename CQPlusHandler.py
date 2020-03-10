# -*- coding:utf-8 -*-
import cqplus
import re
import pypinyin
from bs4 import BeautifulSoup
import requests
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
            return jsonret['data'][0]['v']
        except:
            return "error"


class MainHandler(cqplus.CQPlusHandler):
    def handle_event(self, event, params):
#####
        if event=='on_private_msg':
            msg=params['msg']
            #正则表达式正则表达汉字不是这么用
            if re.search('天气查询',msg,re.I):
                msg=msg[4:]
                self.api.send_private_msg(params['from_qq'],msg)
                w=Weather()
                pinyin=w.invert(msg)
                status=w.getHTMLText()
                if status=='error':
                    self.api.send_private_msg(params['from_qq'],'error happened')
                else:
                    w1=w.fillUnivList()
                    content='今天：'+w1[0]['今天']
                    self.api.send_private_msg(params['from_qq'],content)
            
            if re.search('翻译单词',msg,re.I):
                msg=msg[4:]
                t=Translate()
                res=t.getTranslate(msg)
                self.api.send_private_msg(params['from_qq'],res)
            #else:
            #    self.api.send_private_msg(params['from_qq'], '匹配失败')
#####以上内容为私聊时，若收到消息，将会回复：已接受到消息  匹配成功或匹配失败//吃饭为关键词，收到消息内容含有吃饭就会发送匹配成功。
#####
        if event=='on_group_msg':
            self.api.send_group_msg(params['from_group'],'已接受到消息')
            msg=params['msg']
            if re.search('吃饭',msg,re.I):
                self.api.send_group_msg(params['from_group'], '匹配成功')
            #else:
                #self.api.send_group_msg(params['from_group'], '匹配失败'）
#####以上内容为群聊时，和私聊时所作出反映可以类比
class Weather:

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
            return 'error'


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

