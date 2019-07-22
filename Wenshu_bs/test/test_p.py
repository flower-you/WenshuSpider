#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     :2019/6/15 9:50
# @Author   :17976
# @File     :test_p.py 
# @Description:
import execjs

script = '''function(p, a, c, k, e, r) {
	e = String;
	if ('0'.replace(0, e) == 0) {
		while (c--) r[e(c)] = k[c];
		k = [function(e) {
			return r[e] || e
		}];
		e = function() {
			return '[0]'
		};
		c = 1
	};
	while (c--)
		if (k[c]) p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);
	return p
}('0 dynamicurl="/WZWSREL0xpc3QvTGlzdENvbnRlbnQ=";0 wzwsquestion="y)f;Lvkv8t~YmT+";0 wzwsfactor="2533";0 wzwsmethod="post";0 wzwsparams="Param=%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2%3A%E6%A0%A1%E5%9B%AD%E8%B4%B7&Index=1&Page=1&Order=%E6%B3%95%E9%99%A2%E5%B1%82%E7%BA%A7&Direction=asc&vl5x=23de37f2e4fb9a0603f44ff0&number=T648&guid=c443b5f1-c7e3-085eb34f-c01bd35d8dab";', [], 1, 'var'.split('|'), 0, {})
'''
with open('D:/File/Wenshu_bs/test/ev_p.js', encoding='utf-8') as f:
    jsdata_2 = f.read()
docid_js = execjs.compile(jsdata_2)
res = docid_js.call("evalScript", script)
print(res)