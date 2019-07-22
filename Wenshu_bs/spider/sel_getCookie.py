#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/5/16 13:56
# @Author   :17976
# @File     :sel_getCookie.py 
# @Description:
import random

from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions,FirefoxOptions

def get_proxy():
    proxies =[
        "http://27.25.198.2:9999",
        "http://121.61.0.143:9999",
        "http://183.148.151.216:9999",
        "http://59.62.166.135:9999",
        # "http://116.62.140.147:9999", ecs
        "http://120.78.194.204:80"
    ]
    proxy = random.choice(proxies)
    return proxy


def get_cookie():
    url = "http://wenshu.court.gov.cn/list/list/?sorttype=1"
    # option = webdriver.Chrome()
    # option = ChromeOptions()  # 实例化一个ChromeOptions对象
    option = FirefoxOptions()
    # option.add_argument("excludeSwitches=['enable-automation']")
    option.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 以键值对的形式加入参数
    # proxy = get_proxy()
    proxy = "http://120.83.110.219:9999"
    # print(proxy)
    option.add_argument(f"--proxy-server={proxy}")
    # option = webdriver.Chrome(executable_path='D:/Software/Python27/Scripts/chromedriver.exe', options=option)  # 在调用浏览器驱动时传入option参数就能实现undefined

    option = webdriver.Firefox(executable_path='D:/Software/Python27/Scripts/geckodriver.exe',options=option)
    # option = webdriver.Firefox()

    option.delete_all_cookies()
    option.get(url)
    time.sleep(15)
    cookie_str = ''
    print(option.get_cookies())
    for i in option.get_cookies():
        name = i['name']
        value = i['value']
        str1 = name + '=' + value + '; '
        cookie_str += str1
    print(cookie_str)
    option.close()
    return cookie_str

def get_cookie_dict():
    url = "http://wenshu.court.gov.cn/list/list/?sorttype=1"
    # option = webdriver.Chrome()
    option = webdriver.Firefox()
    option.get(url)
    time.sleep(10)
    # eval = option.find_element('文书ID').text
    # print(eval)
    cookies = {}
    # cookies={"vjkl5": vjkl5, "wzws_cid": wzws_cid}
    for i in option.get_cookies():
        name = i['name']
        value = i['value']
        cookies.update({str(name):str(value)})
    print(cookies)
    option.close()
    return cookies

# def get_cookie():
#     url = "http://wenshu.court.gov.cn/list/list/?sorttype=1"
#     option = webdriver.Ie()
#     option.get(url)
#     time.sleep(25)
#     cookie_str = ''
#     print(option.get_cookies())
#     for i in option.get_cookies():
#         name = i['name']
#         value = i['value']
#         str1 = name + '=' + value + '; '
#         cookie_str += str1
#     print(cookie_str)
#     option.close()
#     return cookie_str

get_cookie()
# get_iecookie()