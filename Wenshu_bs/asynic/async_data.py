#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/25 10:20
# @Author   :17976
# @File     :async_data.py 
# @Description:
import asyncio
import time

from asynic.WenshuSpider import WenshuSpider

start = time.time()

spider = WenshuSpider("校园贷")

loop = asyncio.get_event_loop()  # 建立 事件循环

result = loop.run_until_complete(spider.main())  # 在 事件循环 中执行协程
print(result)

loop.close()  # 关闭 事件循环

total_time = time.time() - start

print(f'total time: {total_time}')