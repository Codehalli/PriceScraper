# The purpose of the program is understand and see how to use web scraping
# in python. This project demonstrated web scraping amazon prices and sending me an
# email when the price of the item went down!
# scraper.py
# By Pranav Rao

import requests  # Installed requests and BS4, requests help get the information
from bs4 import BeautifulSoup  # from a website and BS4 is used to extract that information
import smtplib  # This is built in import that allows us to send/received email
import time  # This will run

# This is the URL that can be replaced on the desired item
URL = 'https://www.amazon.com/Face-Mask-Pack-of-50/dp/B086KMYNSS/ref=sr_1_5?dchild=1&keywords=mask&qid=1593704243&sr' \
      '=8-5 '

# This is the user agent(search on google)
header = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.116 Safari/537.36'}


# This is one module/function
def check_price():
    page = requests.get(URL, headers=header)  # using the request from the URL

    soup = BeautifulSoup(page.content, 'html.parser')  # Parses the Html file

    title = soup.find(id="productTitle").get_text()  # Extract product title
    price = soup.find(id="priceblock_ourprice").get_text()  # Extract  price

    converted_price = float(price[1:3])  # In python to cover string to float

    if converted_price < 29.00:
        send_mail()

    print(converted_price)  # This is for the console output
    print(title.strip())

    if converted_price > 28.00:  # Prints if the price is lower than current price
        send_mail()


# This function is sending email in python
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)  # gmails Server
    server.ehlo()  # Command sent by an email server to identify itself
    server.starttls()  # starts the server
    server.ehlo()  # Command sent by an email server to identify itself

    server.login('raop7495@gmail.com', 'ILkobe!!')  # Got to put in login information

    subject = 'Price is Down!'  # Subject of the Email
    body = 'Check the amazon link https://www.amazon.com/Face-Mask-Pack-of-50/dp/B086KMYNSS/ref=sr_1_5?dchild=1' \
           '&keywords=mask&qid=1593704243&sr=8-5 '  # This is the body where the link to the product is provide

    msg = f"Subject: {subject}\n\n{body}"  # Sending the message in proper subject

    server.sendmail(  # Sending from  and to email addresses
        'prao1524@gmail.com',
        'raop7495@gmail.com',
        msg  # Includes the proper messages
    )

    print('HEY EMAIL HAS BEEN SENT')  # Just for the console/knowing that I was able to send mail

    server.quit()  # This stop the signal of the server


while True:
    check_price()  # Calls the check price function
    time.sleep(86400)  # The time function  allows to say how many time a day
