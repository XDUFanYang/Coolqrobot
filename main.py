# -*- coding: utf-8 -*-
#from cqhttp import CQHttp

from weather import Weather
from translate import Translate
#from CQLog import INFO, WARN
# 引入时间调度器 apscheduler 的 BlockingScheduler
#from apscheduler.schedulers.blocking import BlockingScheduler

w=Weather()
t=Translate()
print(t.getTranslate())
# 与group.py设置一样

