#! /Python

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

def get_ma(stock_code):
    print('Analyzing %s' % stock_code)
    ua_mo = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 Mobile/15B150 Safari/604.1'
    header = {'User-Agent':ua_mo}
    ma_url = 'http://api.finance.ifeng.com/akdaily/?code=%s&type=last' % stock_code
    ma = requests.get(ma_url, headers = header).json()['record']
    # MA5
    ma5_1 = float(ma[-1][8])
    ma5_2 = float(ma[-2][8])
    ma5_3 = float(ma[-3][8])
    ma5_4 = float(ma[-4][8])
    ma5_5 = float(ma[-5][8])
    # MA10
    ma10_1 = float(ma[-1][9])
    ma10_2 = float(ma[-2][9])
    ma10_3 = float(ma[-3][9])
    ma10_4 = float(ma[-4][9])
    ma10_5 = float(ma[-5][9])
    # 
    if ma5_1 < ma10_1:
        if ma5_2 < ma10_2:
            if ma5_3 < ma10_3:
                if ma5_4 < ma10_4:
                    if ma5_5 < ma10_5:
                        fivedays.append(stock_code)
                        print(len(fivedays))


fivedays = []
get_stocks_list()
for i in ashare_list:
    get_ma('sh'+i)




