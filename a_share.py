# !/python

import requests
import pylab as pl

def plot_ma(TITLE, MA5, MA10, DATE):
    pl.title(TITLE)
    a, = pl.plot(DATE, MA5, 'r-')
    b, = pl.plot(DATE, MA10, 'b-')
    pl.legend([a, b], ('MA5', 'MA10'), numpoints=1)
    pl.savefig('stock/%s.png' % TITLE)
    pl.close()
    print('Plot %s success' % TITLE)

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
    ma5_3 = float(ma[-3][8])
    ma5_4 = float(ma[-3][8])
    ma5_average = round((ma5_now+ma5_1+ma5_2+ma5_3+ma5_4)/5, 4)
    # MA10
    ma10_now = float(now[5])
    ma10_1 = float(ma[-1][9])
    ma10_2 = float(ma[-2][9])
    ma10_3 = float(ma[-3][9])
    ma10_4 = float(ma[-3][9])
    ma10_average = round((ma10_now+ma10_1+ma10_2+ma10_3+ma10_4)/5, 4)
    #re = ([ma5_now, ma5_1, ma5_2, ma5_3, ma5_4], [ma10_now, ma10_1, ma10_2, ma10_3, ma10_4])
    re = (ma5_average, ma10_average)
    return re

get_ma(a)

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
    ma5_3 = float(ma[-3][8])
    ma5_4 = float(ma[-4][8])
    ma5_5 = float(ma[-5][8])
    ma5_6 = float(ma[-6][8])
    ma5_7 = float(ma[-7][8])
    ma5_8 = float(ma[-8][8])
    ma5_9 = float(ma[-9][8])
    ma5_10 = float(ma[-10][8])
    # MA10
    ma10_now = float(now[5])
    ma10_1 = float(ma[-1][9])
    ma10_2 = float(ma[-2][9])
    ma10_3 = float(ma[-3][9])
    ma10_4 = float(ma[-4][9])
    ma10_5 = float(ma[-5][9])
    ma10_6 = float(ma[-6][9])
    ma10_7 = float(ma[-7][9])
    ma10_8 = float(ma[-8][9])
    ma10_9 = float(ma[-9][9])
    ma10_10 = float(ma[-10][9])
    if ma[-1][0] == now[0].split()[0]:
        ma5_list = [ma5_1, ma5_2, ma5_3, ma5_4, ma5_5, ma5_6, ma5_7, ma5_8, ma5_9, ma5_10]
        ma10_list = [ma10_1, ma10_2, ma10_3, ma10_4, ma10_5, ma10_6, ma10_7, ma10_8, ma10_9, ma10_10]
        date_list = []
        for i in range(-1, -11, -1):
            date_list.append(ma[i][0].split('-',1)[1])
    else:
        pass
    return(stock_code, ma5_list, ma10_list, date_list)

def plot_images(CODE):
    a = get_ma(CODE)
    plot_ma(a[0], a[1], a[2], a[3])

for i in ashare_list:
    try:
        plot_images('sh'+i)
    except:
        pass
    
    
for i in q3:
    try:
        plot_images(i)
    except:
        pass

