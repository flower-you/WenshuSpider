#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/26 0:02
# @Author   :17976
# @File     :ts1.py 
# @Description:
import time

from pipelines import mongoStore, csv_write
from spider.WenshuSpider import WenshuSpider

# mgStore = mongoStore("校园贷")
# item = mgStore.query_docid("5f012c4c-e88b-4326-91af-aa3900a777c0")
# if str(item) == "None":
#     print("none")

# mgStore = mongoStore("校园贷")
# spider.get_allData()
# for item in mgStore.find_all():
#     print(item["casedocid"])

start = time.time()
spider = WenshuSpider("校园贷")

# store = csv_write("校园贷.csv")

for item in spider.get_allData():
    print(item)
    # store.write_item(item)

print(f'total time: {time.time()-start}')