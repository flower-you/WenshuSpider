#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/19 22:27
# @Author   :17976
# @File     :boot_ui.py 
# @Description:
import os
import sys
import traceback

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from WorkThread import WorkThread
from spider.WenshuSpider import WenshuSpider
from ui.mainwindow1 import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.count = 0

    # @pyqtSlot()
    def show_crawl(self):
        self.search_word = self.word_Edit.text()
        if self.search_word == "" or self.search_word == None:
            QMessageBox.information(self, "提示", "输入不合法！", QMessageBox.OK)

        print(self.search_word)
        self.count_label.setText("开始爬取.......")
        try:
            self.spider = WenshuSpider(self.search_word)
            self.count_label.setText("共采集到" + str(self.spider.count) + "条数据")
        except Exception as e:
            print(repr(e))
            print(traceback.format_exc())

    def init_event(self):
        self.inputok_bt.clicked.connect(self.show_crawl)
        # 将用户定义的changeTitle()函数与单选框的stateChanged()信号连接起来。
        self.word_radio.clicked.connect(self.save_radio)
        self.csv_radio.clicked.connect(self.save_radio)
        self.choose_bt.clicked.connect(self.choose_path)
        self.save_bt.clicked.connect(self.start_download)
        self.quit_bt.clicked.connect(self.closeEvent)

    def save_radio(self, value):
        if self.word_radio.isChecked() == True:
            self.save_type = 'word'
            self.fileName_input.setText(self.search_word+'.docx')
            self.filepath_input.setText(os.getcwd())
            # self.filepath_input.setText(os.getcwd()+"/"+self.filepath_input.text())
        elif self.csv_radio.isChecked() == True:
            self.save_type = 'csv'
            self.fileName_input.setText(self.search_word + '.csv')
            self.filepath_input.setText(os.getcwd())

        else:
            QMessageBox.information(self, "提示", "请选择保存类型！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def choose_path(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self, os.getcwd())
        self.filepath_input.setText(download_path)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出', '确认退出?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def start_download(self):
        try:
            file_name = self.filepath_input.text() + '\\' + self.fileName_input.text()
            self.save_bt.setChecked(True)
            self.save_bt.setDisabled(True)
            self.wthread = WorkThread(self.spider,self.save_type,file_name)
            self.wthread.finishSignal.connect(self.end_download)
            self.wthread.start()
        except Exception as e:
            print(repr(e))
            print(traceback.format_exc())

    def end_download(self):
        self.save_bt.setText(u'下载完成！')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.init_event()
    myWin.show()

    sys.exit(app.exec_())