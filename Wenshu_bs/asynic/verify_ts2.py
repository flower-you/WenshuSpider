#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/6/17 21:18
# @Author   :17976
# @File     :verify_ts2.py 
# @Description:
import asyncio

import aiohttp
import pandas as pd
import numpy as np

# url = "http://wenshu.court.gov.cn/"
url = "http://book.qq.com/"
df = pd.read_csv('ip.csv', header=None, names=["ip", "port"])

proxy_types = ["{}".format(i) for i in np.array(df['ip'])]

ips = ["{}".format(i) for i in np.array(df['ip'])]

ports = ["{}".format(i) for i in np.array(df['port'])]

count = len(ips)

proxy_url = ['http://{0}:{1}'.format( ips[i], ports[i]) for i in range(count)]




headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

async def getsource(proxy):
       conn=aiohttp.TCPConnector(ssl=False)#防止ssl报错
       async with aiohttp.ClientSession(connector=conn) as session: #创建session
             async with session.get(url,headers=headers,proxy=proxy) as req: #获得请求
                 if req.status==200: #判断请求码
                    source=await req.text()#使用await关键字获取返回结果
                    print("成功")
                 else:
                     print("访问失败")

if __name__=="__main__":
         event_loop = asyncio.get_event_loop() #创建事件循环
         tasks = [getsource(proxy) for proxy in proxy_url]
         results = event_loop.run_until_complete(asyncio.wait(tasks))#等待任务结束