# !/Python

from ghost import Ghost, Session
from bs4 import BeautifulSoup
import pytesseract

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'
ua_mo = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 Mobile/15B150 Safari/604.1'
header = {'User-Agent':ua_mo}

gh = Ghost()
se = Session(gh, user_agent=ua, wait_timeout=20, wait_callback=None, display=True, viewport_size=(800, 680), download_images=True)

def login(username, password):
    login = 'https://trade.cgws.com/cgi-bin/user/Login'
    se.open(login)
    se.evaluate("document.getElementById('fundAccount').value='%s'" % username)
    se.evaluate("changeControls('normal');")
    html = se.content
    soup = BeautifulSoup(html, "html.parser")
    keyboard = soup.select('tbody')[0]
    keys = keyboard.select('td')
    for i in range(len(keys)):
        j = (i // 4) + 1
        k = (i % 4) + 1
        globals()['key'+keys[i].text] = "tbody > tr:nth-child(%s) > td:nth-child(%s)" % (j, k)
    for i in password:
        se.click(globals()['key'+i], expect_loading=False)
    se.capture_to('s/a.png', selector='#ticketImg')
    vimage = Image.open('s/a.png')
    vcode = pytesseract.image_to_string(vimage)
    print(vcode)
    se.evaluate("document.getElementById('ticket').value='%s'" % vcode)
    se.click('#submit', expect_loading=True)

def mystock():
    # Mystock
    mystock = 'https://trade.cgws.com/cgi-bin/stock/EntrustQuery?function=MyStock&stktype=0'
    se.open(mystock)
    mystock_html = se.content
    mystock_soup = BeautifulSoup(mystock_html, "html.parser")
    shares = mystock_soup.select('tr.tdheight')
    # Mystock_data
    num = len(shares) - 1
    shares[1].select('td')
    share_code = shares[1].select('td')
    
def myaccount():
    # Myaccount
    myaccount = 'https://trade.cgws.com/cgi-bin/stock/EntrustQuery?function=MyAccount'
    se.open(myaccount)

def sell(code, price, amount):
    sell = 'https://trade.cgws.com/cgi-bin/stock/StockEntrust?function=StockBusiness&type=S'
    se.open(sell)
    if code[0]+code[1] =='60':
        se.evaluate("document.getElementById('secuid').selectedIndex='1'")
    se.evaluate("document.getElementById('stkcode').value='%s'" % code)
    se.evaluate("document.getElementById('price').value='%s'" % price)
    se.evaluate("document.getElementById('amount').value='%s'" % amount)
    se.click('#submit')
    se.show()


user = ''
pw = '102030'
login(user, pw)
