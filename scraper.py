import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL ='https://www.ebay.com/itm/174898650348?epid=170114576&hash=item28b8c59cec:g:b~4AAOSwoGphHZ4y'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", id = "itemTitle").get_text()
    price = soup.find(id = "prcIsum_bidPrice").get_text()[4:]

    if (price < "180"):
        send_mail()

    print(price)
    print(((title.split('  ', 2)[1]))[1:])


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ho.yixuan6@gmail.com', 'gtskkrmmwhzcpvpg')

    subject = 'Price dropped'
    body = 'Visit the link https://www.ebay.com/itm/174898650348?epid=170114576&hash=item28b8c59cec:g:b~4AAOSwoGphHZ4y'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'ho.yixuan6@gmail.com ',
        'sellzunique@gmail.com',
        msg

    )

    print('email sent')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)