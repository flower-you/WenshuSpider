#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/26 18:03
# @Author   :17976
# @File     :ts3.py 
# @Description:
import re

import requests

from spider.sel_getCookie import get_cookie
#
# headers = {
#             'Connection': 'keep-alive',
#             # 'Cookie': self.new_cookie,
#             'Host': 'wenshu.court.gov.cn',
#             'Origin': 'http://wenshu.court.gov.cn',
#             'Referer': "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=UVGSXWVJ&guid=aabc33f0-863f-b511e395-6b23ddeda3f3&conditions=searchWord+QWJS+++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E6%A0%A1%E5%9B%AD%E8%B4%B",
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
#         }
# url = "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=UVGSXWVJ&guid=aabc33f0-863f-b511e395-6b23ddeda3f3&conditions=searchWord+QWJS+++%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2:%E6%A0%A1%E5%9B%AD%E8%B4%B7"
#
# headers = {
#             'Connection': 'keep-alive',
#             # 'Cookie': self.new_cookie,
#             'Host': 'wenshu.court.gov.cn',
#             'Origin': 'http://wenshu.court.gov.cn',
#             'Referer':"http://wenshu.court.gov.cn/",
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
#         }
# url2 = "http://wenshu.court.gov.cn"
# res2 = requests.get(url2,headers=headers)
# raw_func = re.findall(r'<script type="text/javascript">(.*)</script>',res2.text,re.DOTALL)[0]
# print(res2.cookies)
# print(res2.text)
# print(raw_func)

url3 = "http://wenshu.court.gov.cn/WZWSREL2NvbnRlbnQvY29udGVudD9Eb2NJRD0yNDU0MTc4MC0xY2Q4LTRjNGItYTk0Mi1hODUxMDBhYzYwNWQmS2V5V29yZD0lRTYlQTAlQTElRTUlOUIlQUQlRTglQjQlQjc="
headers = {
            'Connection': 'keep-alive',
            'Cookie': get_cookie(),
            'Host': 'wenshu.court.gov.cn',
            'Origin': 'http://wenshu.court.gov.cn',
            'Referer':"http://wenshu.court.gov.cn/",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        }
res3 = requests.get(url=url3,headers=headers)
print(res3.headers)
print(location = res3.headers['Location'])