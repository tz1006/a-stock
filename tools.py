# !/Python

import requests

def sscode(code):
    if str(code)[0]+str(code)[1] =='60':
        code = 'sh%s' % code
    else:
        code = 'sz%s' % code
    return code

def stock_name(code):
    s = requests.session()
    s.keep_alive = False
    url = 'http://hq.sinajs.cn/list=%s' % sscode(code)
    r = None
    while r == None:
        r = s.get(url, timeout=2)
    name = r.text.split("\"")[1].split(",",1)[0]
    return name


