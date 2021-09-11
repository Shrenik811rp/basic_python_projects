import requests
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal
import smtplib




url = 'https://www.flipkart.com/asus-tuf-gaming-f17-2021-core-i5-11th-gen-8-gb-1-tb-ssd-windows-10-home-4-gb-graphics-nvidia-geforce-rtx-3050-144-hz-fx706hc-hx070t-laptop/p/itmce7443dfb4e63?pid=COMG3ZF8XHHDEMTV&lid=LSTCOMG3ZF8XHHDEMTVFXM49Y&marketplace=FLIPKART&q=asus+laptop&store=6bo%2Fb5g&srno=s_1_21&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&fm=SEARCH&iid=762c96be-f3eb-4739-a32b-b2f08adfbda6.COMG3ZF8XHHDEMTV.SEARCH&ppt=sp&ppn=sp&ssid=19ix4ou6j40000001631380945360&qH=cda2435f700c2043'



headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}



def check_price():
    page = requests.get(url,headers=headers)


    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find('span', {'class' : "B_NuCI"}).get_text()

    price = soup.find('div', {'class' : "_30jeq3 _16Jk6d"}).get_text()

    converted_price = float(Decimal(sub(r'[^\d.]', '', price)))
    print(converted_price)

    print(title)

    if (converted_price < 90000):
        send_mail()



def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)

    server.ehlo()
    server.starttls()
    server.ehlo()
    #IF LESS SECURE APP IS ENABLED USE GMAIL PASSWORD
    #ELSE USE SECURE APP PASSWORDS AFTER 2 STEP VERIFICATION
    server.login('SENDER_EMAIL_ADDRESS','PASSWORD')

    subject = 'Price fall'
    body = "Check link: https://www.flipkart.com/asus-tuf-gaming-f17-2021-core-i5-11th-gen-8-gb-1-tb-ssd-windows-10-home-4-gb-graphics-nvidia-geforce-rtx-3050-144-hz-fx706hc-hx070t-laptop/p/itmce7443dfb4e63?pid=COMG3ZF8XHHDEMTV&lid=LSTCOMG3ZF8XHHDEMTVFXM49Y&marketplace=FLIPKART&q=asus+laptop&store=6bo%2Fb5g&srno=s_1_21&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&fm=SEARCH&iid=762c96be-f3eb-4739-a32b-b2f08adfbda6.COMG3ZF8XHHDEMTV.SEARCH&ppt=sp&ppn=sp&ssid=19ix4ou6j40000001631380945360&qH=cda2435f700c2043"

    msg = f'subject:{subject}\n\n{body}\n'

    server.sendmail(
        'SENDER_EMAIL_ADDRESS',
        'RECIEVER_EMAIL_ADDRESS',
        msg
    )

    print("Email sent")
    server.quit()



check_price()