import requests
from bs4 import BeautifulSoup
import time
import smtplib
import sys

while True:
    url = "https://www.jcrew.com/p/mens_category/shoes/sneakers/nike-for-jcrew-killshot-2-sneakers/85231"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    if str(soup).find("add to bag") == -1:
        time.sleep(10800)
        continue

    else:
        password = sys.argv[2]
        msg = "Check JCrew for Killshots!"
        fromaddr = sys.argv[1]
        toaddr = sys.argv[1]

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(fromaddr, password)

        server.sendmail(fromaddr, toaddr, msg)
        server.quit()

        break
