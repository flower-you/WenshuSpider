# #!/usr/bin/env python
# # -*- coding:utf8 -*-
# # @TIME     :2019/5/24 20:46
# # @Author   :17976
# # @File     :async_spider.py
# # @Description:
# #!/usr/bin/env python
# # -*- coding:utf8 -*-
# # @TIME     :2019/5/17 21:31
# # @Author   :17976
# # @File     :WenshuSpider.py
# # @Description:文书主题爬虫
# import asyncio
# import json
# import re
# import time
#
# import aiohttp
# import execjs
# import math
# import requests
#
# from items import WenshuCaseItem
# from pipelines import mongoStore, csv_write
# from spider.sel_getCookie import get_cookie, get_cookie_dict
#
#
# class WenshuSpider():
#
#     def __init__(self,search_word,file_name):
#         with open('../spider/get_vl5x.js', encoding='utf-8') as f:
#             jsdata_1 = f.read()
#         with open('../spider/get_docid.js', encoding='utf-8') as f:
#             jsdata_2 = f.read()
#         with open('../spider/get_guid.js', encoding='utf-8') as f:
#             jsdata_3 = f.read()
#         self.vl5x_js = execjs.compile(jsdata_1)
#         self.docid_js = execjs.compile(jsdata_2)
#         self.guid_js = execjs.compile(jsdata_3)
#         self.guid = self.guid_js.call('getGuid')
#         self.search_word = search_word
#         self.file_name = file_name
#         # self.mt = mongoStore(self.search_word)
#         self.new_cookie = get_cookie()
#         self.count =  self.get_count()
#
#
#     def get_count(self):
#         # 首先获取案件总数
#         try:
#             headers = {
#                 'Connection': 'keep-alive',
#                 'Cookie': self.new_cookie,#scrapy中为字典形式
#                 #headers中的cookie要求为字符串形式，将cookies单独写出来需要是字典的形式
#                 'Host': 'wenshu.court.gov.cn',
#                 'Origin': 'http://wenshu.court.gov.cn',
#                 'Referer': "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=T648SFX6",
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
#             }
#             vjkl5 = re.search('vjkl5=(.*?);', self.new_cookie).group(1) #cookie为字符串形式
#             # vjkl5 = self.new_cookie['vjkl5'] #cookie为字典形式
#             url = 'http://wenshu.court.gov.cn/List/ListContent'
#             vl5x = self.vl5x_js.call('getKey', vjkl5)
#
#             data = {'Param': '全文检索:{}'.format(self.search_word),
#                     'Index': '1',
#                     'Page': '1',
#                     'Order': '法院层级',
#                     'Direction': 'asc',
#                     'vl5x': vl5x,
#                     'number': 'T648',  # random.random(),
#                     'guid': self.guid
#                     }
#             res = requests.post(url=url, headers=headers, data=data)
#             json_str = json.loads(res.text.strip('"').replace('\\', ''))
#             # print(json_str)
#             self.count = int(json_str[0][u'Count'])
#             print(self.count)
#             return self.count
#         except:
#             # 失败则重新获取cookie请求
#             print("get_count expect")
#             self.new_cookie = get_cookie()
#             return self.get_count()
#
#
#     '''调用get_count得到案件总数之后调用get_list,循环得到所有列表页的数据'''
#     async def get_list(self, index):
#         '''获取一页的数据，index：第几页'''
#         headers = {
#             'Connection': 'keep-alive',
#             'Cookie': self.new_cookie,
#             'Host': 'wenshu.court.gov.cn',
#             'Origin': 'http://wenshu.court.gov.cn',
#             'Referer': "http://wenshu.court.gov.cn/list/list/?sorttype=1&number=T648SFX6",
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
#         }
#         vjkl5 = re.search('vjkl5=(.*?);', self.new_cookie).group(1)
#         url = 'http://wenshu.court.gov.cn/List/ListContent'
#
#         data = {'Param': '全文检索:{}'.format(self.search_word),
#                 'Index': str(index),
#                 'Page': '20',  # 最多20
#                 'Order': '法院层级',
#                 'Direction': 'asc',
#                 'vl5x': self.vl5x_js.call('getKey', vjkl5),
#                 'number': 'T648',  # random.random(),
#                 'guid': self.guid
#                 }
#
#         res_list = requests.post(url=url, headers=headers, data=data)
#         if "请开启JavaScript并刷新该页" in res_list.text:
#             self.new_cookie = get_cookie()
#             return self.get_list(index)
#         elif len(eval(json.loads(res_list.text))[0]) < 2:
#             return self.get_list(index)
#         else:
#             json_str = json.loads(res_list.text.strip('"').replace('\\', ''))
#             # print(json_str)
#             return json_str
#
#
#
#
#     '''再得到列表页的数据之后调用这个方法get_detail'''
#     async def get_detail(self,loop,session, json_str):
#         '''获取文书id,请求并返回案件详情页'''
#         run_eval = json_str[0].get("RunEval", "")
#         content = json_str[1:]  #遍历列表中的案件
#         for i in content:
#             docid = self.get_docid(i, run_eval)
#             yield docid
#
#         for doc_ids in done:
#             tasks.append(self.req_detail(session,doc_ids.result()))
#         # 执行并等待所有任务完成
#         done, _ = await asyncio.wait(tasks)
#         # 获取所有返回结果
#         items = [f.result() for f in done]
#         print(type(items))
#         # result = loop.run_until_complete(asyncio.gather(*tasks))
#         return items
#
#
#     def get_docid(self,content,run_eval):
#         docid = content.get(u'文书ID')
#         casejudgedate = content.get(u'裁判日期')
#
#         js = self.docid_js.call("GetJs", run_eval)
#         js_objs = js.split(";;")
#         js1 = js_objs[0] + ';'
#         js2 = re.findall(r"_\[_\]\[_\]\((.*?)\)\(\);", js_objs[1])[0]
#         key = self.docid_js.call("EvalKey", js1, js2)
#         key = re.findall(r"\"([0-9a-z]{32})\"", key)[0]
#         docid = self.docid_js.call("DecryptDocID", key, docid)
#         print('*************文书ID:' + docid)
#         return docid
#
#
#     async def req_detail(self, session,docid):
#         '''获取每条案件详情'''
#         try:
#             detail_url = 'http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID=' + str(docid)
#             headers = {
#                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
#                 "Cookie": self.new_cookie,
#                 "Referer": "http://wenshu.court.gov.cn/content/content?DocID={}&KeyWord=%E6%A0%A1%E5%9B%AD%E8%B4%B7".format(
#                     docid)
#             }
#             async with session.get(
#                     # 这里的timecout一定要设置
#                     detail_url, headers= headers, timeout=aiohttp.ClientTimeout(total=5)
#             ) as response:
#                 if response.status == 200:
#                     detail_resp =  await response.text()
#                     if "请开启JavaScript并刷新该页" in detail_resp:
#                         session = aiohttp.ClientSession(cookies= get_cookie_dict())
#                         self.new_cookie = get_cookie()
#                         return await self.req_detail(session,docid)
#                     else:
#                         item = self.parse_detail(detail_resp)
#                         return item
#                 else:
#                     return "expect"
#         except:
#             return await self.req_detail(session,docid)
#
#
#     def parse_detail(self, detail_resp):
#         content_1 = json.loads(re.search(r'JSON\.stringify\((.*?)\);\$\(document', detail_resp).group(1))  # 内容详情字典1
#         content_3 = re.search(r'"Html\\":\\"(.*?)\\"}"', detail_resp).group(1)  # 内容详情字典3(doc文档正文)
#         reg = re.compile(r'<[^>]+>', re.S)
#
#         # 存储到item
#         item = WenshuCaseItem()
#
#         item['casecourt'] = {
#             'casecourtid': content_1.get('法院ID', ''),
#             'casecourtname': content_1.get('法院名称', ''),
#             'casecourtprovince': content_1.get('法院省份', ''),
#             'casecourtcity': content_1.get('法院地市', ''),
#             'casecourtdistrict': content_1.get('法院区县', ''),
#             'casecourtarea': content_1.get('法院区域', ''),
#         }
#         item['casecontent'] = {
#             'casebasecontent': content_1.get('案件基本情况段原文', ''),
#             'caseaddcontent': content_1.get('附加原文', ''),
#             'caseheadcontent': content_1.get('文本首部段落原文', ''),
#             'casemaincontent': content_1.get('裁判要旨段原文', ''),
#             'casecorrectionscontent': content_1.get('补正文书', ''),
#             'casedoccontent': content_1.get('DocContent', ''),
#             'caselitigationcontent': content_1.get('诉讼记录段原文', ''),
#             'casepartycontent': content_1.get('诉讼参与人信息部分原文', ''),
#             'casetailcontent': content_1.get('文本尾部原文', ''),
#             'caseresultcontent': content_1.get('判决结果段原文', ''),
#             'casestrcontent': reg.sub('', content_3),  # 去除html标签后的文书内容
#         }
#         item['casetype'] = content_1.get('案件类型', '')  # 案件类型
#         # item['casejudgedate'] = response.meta['casejudgedate']  # 裁判日期
#         item['caseprocedure'] = content_1.get('审判程序', '')
#         item['casenumber'] = content_1.get('案号', '')
#         item['casenopublicreason'] = content_1.get('不公开理由', '')
#         item['casedocid'] = content_1.get('文书ID', '')
#         item['casename'] = content_1.get('案件名称', '')
#         item['casecontenttype'] = content_1.get('文书全文类型', '')
#         item['caseuploaddate'] = time.strftime("%Y-%m-%d",
#                                                time.localtime(int(content_1['上传日期'][6:-5]))) if 'Date' in content_1[
#             '上传日期'] else ''
#         item['casedoctype'] = content_1.get('案件名称').split('书')[0][-2:] if '书' in content_1.get(
#             '案件名称') else '令'  # 案件文书类型:判决或者裁定...还有令
#         item['caseclosemethod'] = content_1.get('结案方式', '')
#         item['caseeffectivelevel'] = content_1.get('效力层级', '')
#
#         return item
#
#
#     async def get_allData(self):
#         page = math.ceil(int(self.count) / 100)
#         if page > 0:
#             for i in range(1, int(page) + 1):
#                 res_list = self.get_list(i)
#                 print(res_list)
#                 await  self.get_detail(res_list)
#         # self.mt.close_client()
#
#
#     async def main(self,loop):
#         page = math.ceil(int(self.count) / 20)
#         if page > 0:
#             async with aiohttp.ClientSession(cookies= get_cookie_dict()) as session:
#                 tasks = []
#                 for i in range(1,  int(page) + 1):
#                     # res_list = await self.get_list(session, i)
#                     # print(res_list)
#                     tasks.append(self.get_list(i))
#                 done, _ = await asyncio.wait(tasks)
#                 for res_list in done:
#                     res = await self.get_detail(loop, session, res_list.result())
#                     print(res)
#
#
#
