#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/25 21:19
# @Author   :17976
# @File     :WorkThread.py 
# @Description:
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal

from pipelines import DocStore, csv_write, mongoStore


class WorkThread(QThread):
    # 使用信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
    finishSignal = pyqtSignal(str)
    # 带参数示例
    def __init__(self,spider, save_type,file_path,parent=None):
        super(WorkThread, self).__init__(parent)
        self.save_type = save_type
        self.file_name = file_path
        self.spider = spider

        if self.save_type == 'word':
            self.store = DocStore(self.file_name)
        elif self.save_type == 'csv':
            self.store = csv_write(self.file_name)


    def run(self):
        for item in self.spider.get_allData():
            print(item)
            self.store.write_item(item)

        if self.save_type == 'word':
            self.store.complete()

        self.finishSignal.emit('finish')
        # return
