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
        code = stock_data[i]['SECURITY_CODE_A']
        name = stock_data[i]['SECURITY_ABBR_A']
        totalFlowShares = stock_data[i]['totalFlowShares']
        totalShares = stock_data[i]['totalShares']
        listing_date = stock_data[i]['LISTING_DATE']
        ashare_list.append(code)
        insert_data(code, name, totalFlowShares, totalShares, listing_date)
        print(code, name, totalFlowShares, totalShares, listing_date)
    print('Found %d Stocks!' % len(stock_data))

def delete_form(form):
    conn = sqlite3.connect('database/ss.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS %s;" % form)
    conn.commit()
    conn.close()
    print("%s Deleted!" % form)

def create_form(form):
    conn = sqlite3.connect('database/ss.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS %s
        (CODE INTEGER PRIMARY KEY UNIQUE,
        NAME   TEXT,
        FLOWSHARES   REAL,
        TOTALSHARES   REAL,
        LISTING_DATE   TEXT);''' % form)
    conn.commit()
    conn.close()
    print("%s Created!" % form)

def insert_data(id, name, flowshares, totalshares, listing_date):
    conn = sqlite3.connect('database/ss.db')
    c = conn.cursor()
    c.execute("INSERT INTO A_SHARE (CODE, NAME, FLOWSHARES, TOTALSHARES, LISTING_DATE) VALUES (?, ?, ?, ?, ?)",(id, name, flowshares, totalshares, listing_date))
    conn.commit()
    conn.close()

delete_form('A_SHARE')
create_form('A_SHARE')
get_stocks_list()

# url = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback86157&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25'
