#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/17 23:59
# @Author   :17976
# @File     :items.py 
# @Description:
import scrapy


class WenshuCaseItem(scrapy.Item):
    # define the fields for your item here like:
    casecourt = scrapy.Field()#法院信息
    casecontent = scrapy.Field()#案件内容
    casetype = scrapy.Field()#案件类型
    # casereason = scrapy.Field()
    casejudgedate = scrapy.Field()
    # caseparty = scrapy.Field()
    caseprocedure = scrapy.Field()#审判程序
    casenumber = scrapy.Field()#案号
    casenopublicreason = scrapy.Field()#不公开理由
    casedocid = scrapy.Field()
    casename = scrapy.Field()
    casecontenttype = scrapy.Field()
    caseuploaddate = scrapy.Field()
    casedoctype = scrapy.Field()#文书全文类型
    caseclosemethod = scrapy.Field()#结案方式
    caseeffectivelevel = scrapy.Field()#效力层级
