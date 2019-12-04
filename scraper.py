import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL ='https://www.amazon.com/Canon-T6-Digital-Telephoto-Accessory/dp/B01D93Z89W/ref=sxin_2_osp48-fd978382_cov?ascsubtag=fd978382-76a6-478f-a63a-61423996920f&creativeASIN=B01D93Z89W&cv_ct_id=amzn1.osp.fd978382-76a6-478f-a63a-61423996920f&cv_ct_pg=search&cv_ct_wn=osp-search&keywords=camera&linkCode=oas&pd_rd_i=B01D93Z89W&pd_rd_r=4582e235-cfdb-494d-9a08-a6ec09207557&pd_rd_w=FSXjU&pd_rd_wg=ndVmP&pf_rd_p=01a10a0c-41cd-43e7-9966-cab0d3a2d561&pf_rd_r=MK4JFAF6MM2Q63FZC7MB&qid=1567014723&s=gateway&tag=spyonsite-20'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:4])

    if(converted_price < 440):
            send_mail()

    print(converted_price)
    print(title.strip())
       

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    email = "your email here"
    password = "your password here"
    
    server.login( email, password )

    subject = "Price fell down!"
    body = "BUY! BUY! BUY!"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mreamer24@gmail.com',
        'reamer.m.p@gmail.com',
        msg
        )
    print("email sent")
    server.quit()

while(True):
    check_price()
    time.sleep(86400)
    