# -*- coding: utf-8 -*-

import threading

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import datetime


class Huanqiu():
    url = "http://s.huanqiu.com/s?q="

    @classmethod
    def getone(cls, url):
        # 从一个新闻页面获取新闻题目，内容，时间
        r = requests.get(url)
        soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
        temp = soup.find('h1', {'class': 'tle'})
        if temp is not None:
            title = temp.text
        else:
            title = 'NONE'
        temp = soup.find('span', {'class': 'la_t_a'})
        if temp is not None:
            time = temp.text
        else:
            time = 'NONE'
        temp = soup.find('div', {'class': 'la_con'})
        if temp is not None:
            content = ' '.join(map(lambda x: x.text, temp.findAll('p')[:-1]))
        else:
            content = "NONE"
        return title, content, time

    @classmethod
    def getmin(cls, minurl):
        ret = []
        r = requests.get(minurl)
        soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')
        h3 = soup.findAll("h3")
        for h3i in h3:
            h3ia = h3i.find(href=re.compile(".html$"))
            if h3ia is not None:
                href = h3ia['href']
                print(href)
                tle, con, tim = cls.getone(href)
                if tle is not "NONE":
                    ret.append({"title": tle, "content": con, "time": tim, "url": href})
        return ret

    @classmethod
    def loop(cls, url, i):
        result = cls.getmin(url)
        print(result.to_json())
        result.to_csv('./huanqiu/result' + str(i) + '.csv', index=False)

    @classmethod
    def main(cls):
        ts = []
        i = 0
        for url in cls.urls[:10]:
            i += 1
            ts.append(threading.Thread(target=cls.loop, args=(url, i), name='LoopThread'))
        for t in ts:
            t.start()
        for t in ts:
            t.join()

    @classmethod
    #此处是网站调用爬虫的开始
    def get_huanqiu_news(cls, key="南海", start_time=None, end_time=None):
        # start_time="2019-05-01 13:26:56"
        ret = []
        if start_time is not None:
            start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        else:
            start_time = datetime.datetime(1999, 1, 1, 0, 0)
        if end_time is not None:
            end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        else:
            end_time = datetime.datetime(2999, 1, 1, 0, 0)
        for i in range(1, 5):
            ret += Huanqiu.getmin(Huanqiu.url + key + "&p=" + str(i))
        news_id = 1
        ret2 = []
        for i in ret:
            t = datetime.datetime.strptime(i['time'], "%Y-%m-%d %H:%M")
            if start_time < t < end_time:
                i["id"] =news_id
                news_id += 1
                ret2.append(i)
        nid,title, content, time, url,language,event = [], [], [], [],[],[],[]
        index=0
        for i in ret2:
            nid.append("huanqio-"+i['time']+"-"+str(index))
            index=index+1
            title.append(i['title'])
            content.append(i['content'])
            time.append(i['time'])
            url.append(i['url'])
            language.append("chinese")
            event.append(key)
        result = pd.DataFrame({"nid":nid,"title": title, "content": content, "time": time, "url": url,"language":language,"event":event})
        print(result)
        result.to_csv("./new.csv")

        return ret2


if __name__ == '__main__':
    ret = Huanqiu.get_huanqiu_news(key="南海问题")
    title, content, time, url = [], [], [], []
    for i in ret:
        title.append(i['title'])
        content.append(i['content'])
        time.append(i['time'])
        url.append(i['url'])
    result = pd.DataFrame({"title": title, "content": content, "time":time, "url": url})
    print(result)
    result.to_csv("new.csv")
    # print(Huanqiu.getone('http://mil.huanqiu.com/world/2019-05/14843637.html'))
