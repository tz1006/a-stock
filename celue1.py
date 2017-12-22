# !/Python

import requests
import sqlite3

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


