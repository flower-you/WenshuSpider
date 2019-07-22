#!/usr/bin/env python
# -*- coding:utf8 -*-

import re

import execjs
def get_docid(docid,run_eval):
    js = docid_js.call("GetJs", run_eval)
    print(str(js))
    js_objs = js.split(";;")
    hidescript = js_objs[0] + ';'
    print(str(hidescript))
    # 得到匿名函数的内容
    print(js_objs[1])
    func = re.findall(r"_\[_\]\[_\]\((.*?)\)\(\);", js_objs[1])[0]
    print("匿名函数内容："+str(func))
    # 返回解密之后的匿名函数内容
    anonymous_func = docid_js.call("EvalKey", hidescript, func)
    print("解密之后的匿名函数"+anonymous_func)
    # 正则匹配具体key值
    key = re.findall(r"\"([0-9a-z]{32})\"", anonymous_func)[0]
    print("密匙：" + str(key))
    print("加密的文书ID:"+docid)
    docid = docid_js.call("DecryptDocID", key, docid)
    print('解密出的文书ID:' + docid)
    return docid

with open('D:/File/Wenshu_bs/spider/get_docid.js', encoding='utf-8') as f:
    jsdata_2 = f.read()
docid_js = execjs.compile(jsdata_2)
RunEval= "w61ZS27CgzAQPQtRFsK2wqhyAcKUVcKOw5DDpcOIQhFJExYJwpVDV1HDrh7CoCnDpWMIFMKbwpjDsiQ0CHs+b8KeBzMWw4tjwrjDm18CGX7DhsOrw7dYwobDp8ODw6pDRsKnw41xKzfDkW7Dj1zDhyUBYcK1eAMJEMOzwqjCkMO/wpDDiExeV8OsSlhbCMOwDmYhwrB6YAzCiwt2QAI4QcOWSBhMIH8QA8KewpAcUsOCCkDCoBDCrBLDnMOzw7zDtSLCiMOOwpdYfgVxJBfCnk/Cvkguw4bDnMOrLVXDi8Kvw6vCjcOTwrclJUIIwpc5w5kEwqfCssOPdMOiw7lMw7bCuMO8w70nTSwdTjTDiElnSFBywqsELMKrOw/Cg8OmYBXDnErDnVZMRW/DqsOxPFTChsK6TlENwoIywocWw585w4huwowWHsKfw4LDrsKow5FHwq3Ct8Ouw58MBlgNNcOVYsKvw4/CiWZPw5Vqw5MMwpPDvWwmwpTCvcOcwqYSMMOmw5PCrMOjKXs3C1tzCMOTHMKPWcOmwprCs8KaQMKBw5gNwrHCuRcwwrHDhTXDth0tHRjDtcOqD17CuSAjw4TDkcO/w6nCpMK8w6MbwokgK8KaGS3DgUZFMsO5w5LChcOjCcKEfcOEwq7DrsK6wp3DjsKcFnHCozhYw5ZSwqJSw5PCox4tOsKkAUfDo8KXUzZXFMKCM8Ouw50B"
docid =  "DcKNwrkNw4BADMODVsOyf3bDqXfDv8KREsKoEkBRw6kJMFJuVgIvwppyw5HCpMO0w6IQb8OJOHXCn8OsFgFrwoTDqsOgw4NxR8OtaMORIsOMwqkdW8O7wqspw5HDplXCinRHasO/O34nP8Kfw6Rgd8Omw47Dm2fDhsOEwqBvw77DuCQ7HwR0e8KJw4BvwrN2JQgrwo5cw7jDv8KAeAvDimEewpPCm3fDkcOswrEpDzDCoHo/wpoWw5kgwoLCl8Kqw4hpw6Yf"
docid = get_docid(docid,RunEval)



