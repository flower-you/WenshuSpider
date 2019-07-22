#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/18 10:33
# @Author   :17976
# @File     :get_data.py 
# @Description:
import os
import time

from pipelines import DocStore
from asynic.WenshuSpider import WenshuSpider


def main():

    search_word = "校园贷"
    file_name = '校园贷.docx'
    spider = WenshuSpider(search_word)
    print(spider.count)
    print("==================get_data=======================")
    # with open(file_name, 'a+', encoding='utf-8-sig') as f:
    #     pass
    store = DocStore(file_name)
    # # store = csv_write('D:/File/Wenshu_bs/校园贷.docx')
    for item in spider.get_allData():
        print(item)
        store.write_item(item)

def get_path():
    print(os.getcwd())
    return os.getcwd()

def thread_demo(n):
   while n >= 0:
       print("n:", n)
       n -= 1
       time.sleep(1)

if __name__ == '__main__':
    # t = threading.Thread(target=thread_demo, args=(10,))
    # t.start()
    # t.join()
    # print("exit")
    start = time.time()
    main()
    total_time = time.time() - start
    print(f'total time: {total_time}')