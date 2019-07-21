# -
2019.4.20-2019.5.21     基于主题的裁判文书数据采集系统    
开发环境：PyCharm+Python3.7+Anaconda3+NodeJS10.15.3+Selenium3.14+PyQt5+MongoDB4.0.9 
项目描述：    使用python编写的主题爬虫，可以根据用户输入的关键字采集中国裁判文书网(http://wenshu.court.gov.cn/)中相关的的裁判文书。系统使用pyQt5做界面，使用NodeJs处理参数加密，使用Selenium获取cookie, 使用协程+aiohttp搭建简易的用户代理池，使用MongoDB作为内部存储，给用户提供csv和word两种存储方式，word文档可以创建良好的索引信息，便于快速定位文书信息。    中国裁判文书网的反爬十分严格，使用了大量的Js加密，列表页和详情页加密都十分复杂，使用了多种加密算法混合， sha1,md5,base64,hex,aes,JsFuck等,列表页是一个Ajax请求，vl5x参数会根据cookie结合各种随机的加密算法进行加密。 由于cookie加密方式太过复杂，且加密方式更新十分频繁，cookie加密未能破解最终使用selenium来获取cookie。

