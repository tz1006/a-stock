import requests
import sqlite3
from bs4 import BeautifulSoup
import threading

def get_stocks_list():
    global ashare_list
    ashare_list = []
    url = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&stockType=1&pageHelp.beginPage=1&pageHelp.pageSize=2000'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/',
    }
    stock_data = requests.get(url, headers = header).json()['pageHelp']['data']
    for i in range(len(stock_data)):
        print(i)
        code = stock_data[i]['SECURITY_CODE_A']
        listing_date = stock_data[i]['LISTING_DATE']
        if listing_date != '-':
            d = listing_date.split('-')
            n = int(d[0]+d[1]+d[2])
            if n < 20171201:
                ashare_list.append(code)
                print('%s Added!' % code)
    print('Found %d Stocks!' % len(ashare_list))

get_stocks_list()

def check_stop(stock_code):
    print('Checking Stop %s...' % stock_code)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    url = 'http://finance.ifeng.com/app/hq/stock/sh%s/' % stock_code
    html = None
    while html == None:
        html = requests.get(url, headers=header, timeout=3).content
    soup = BeautifulSoup(html, "html.parser")
    stop = soup.select('td.Hfont')[0].text
    if stop == '停牌':
        ashare_list.remove(stock_code)

threads = []
for i in ashare_list:
    a = threading.Thread(target=check_stop, args=(i,))
    threads.append(a)
    a.start()

for t in threads:
    t.join()

for i in ashare_list:
    check_stop(i)

q = []

def get_ma(stock_code):
    ua_mo = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 Mobile/15B150 Safari/604.1'
    header = {'User-Agent':ua_mo}
    ma_url = 'http://api.finance.ifeng.com/akdaily/?code=%s&type=last' % stock_code
    now_url = 'http://api.finance.ifeng.com/aminhis/?code=%s&type=five' % stock_code
    now = requests.get(now_url, headers = header).json()[-1]['record'][-1]
    ma = requests.get(ma_url, headers = header).json()['record']
    # MA5
    ma5_now = float(now[4])
    ma5_1 = float(ma[-1][8])
    ma5_2 = float(ma[-2][8])
    # MA10
    ma10_now = float(now[5])
    ma10_1 = float(ma[-1][9])
    ma10_2 = float(ma[-2][9])
    # 
    if (ma5_now > ma10_now and ma5_1 < ma10_1) or (ma5_now < ma10_now and ma5_1 > ma10_1):
        print('金叉符合')
        if ma5_now > ma5_1 > ma5_2:
            print('MA5上涨2天符合')
            if ma10_now > ma10_1:
                print('MA10上涨1天符合')
                q.append(stock_code)
                print('----------完全符合--------- %s' % stock_code)

for i in ashare_list:
    print('Analyzing %s' % i)
    try:
        get_ma('sh'+i)
    except:
        pass
    else:
        print('Fail %s' % i)



    re = (ma5_average, ma10_average)
    return re
