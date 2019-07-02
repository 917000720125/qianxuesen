# 插入测试数据
from django.db import connection
import random
ssql = '''INSERT INTO huanqiu_news (news_name,news_content,time) VALUES ("{0}","{1}","{2}")'''

for i in range(200):
    with connection.cursor() as cursor:
        cursor.execute(ssql.format("新闻名称"+str(i), "新闻内容"+str(i), "2019-04-"+str(random.randint(1, 30)).rjust(2, '0')))

ssql='''INSERT INTO `huanqiu_news_associated` (`newid`, `cno`, `newtopic`, `emotional_words`, `emotional_plus_or_minus`, `probability`) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')'''
for i in ('1111','2222','3333','4444'):
    newids=set()
    for j in range(60):
        newids.add(random.randint(5, 200))
    for jj in newids:
        with connection.cursor() as cursor:
            cursor.execute(ssql.format(str(jj), i, "newtopic", "emotionalwords",
                                       str(random.randint(0, 1)*2-1),str(random.random())))

# 新闻表测试数据
from News.models import *
import time
import datetime
import random
s = time.mktime((2018,1,1,0,0,0,0,0,0))
e = time.mktime((2018,12,31,0,0,0,0,0,0))
for i in range(300):
    data = News()
    data.id = i
    data.title = "新闻标题" + str(i)
    data.content = ("新闻内容" + str(i)) * 5
    data.time = datetime.datetime.fromtimestamp(random.randint(s, e))
    data.source = "环球网"
    data.emotional_words = "情感词" + str(random.randint(1, 10))
    data.emotional_express = "情感表达者" + str(random.randint(1, 10))
    data.emotional_express_class = "情感表达者类别" + str(random.randint(1, 10))
    data.emotional_event = "情感事件" + str(random.randint(1, 10))
    data.emotional_plus_or_minus = 2*random.randint(0, 1)-1
    data.probability = random.random()
    data.language = "中文"
    data.save()


