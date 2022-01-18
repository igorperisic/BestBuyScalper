import requests
import pprint
import smtplib
import webbrowser  
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


def notif(body):
    #The mail addresses and password
    sender_address = 'sender email address'
    sender_pass = 'sender email password'
    recipients = ['recipient1','recipient2']

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = ", ".join(recipients)
    message['Subject'] = 'email subject'   #The subject line

    #The body and the attachments for the mail
    message.attach(MIMEText(body, 'plain'))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, recipients, text)
    session.quit()

def openPage():
    webbrowser.open('https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440', new=0, autoraise=True) #opens product page
    webbrowser.open('https://api.bestbuy.com/click/5592e2b895800000/6429440/cart', new=0, autoraise=True)   #opens Add to Cart page

def webAccess():
    url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}

    response = requests.get(url, headers=headers)

    status = ""

    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find_all("button", {"style": "padding:0 8px"})

    for res in div:
        status =  status + str(res.text)
        return status
        
i = 1
while i == 1:
    try:
        status = webAccess()
        if status != 'Sold Out':
            mail_content = "The Product is in Stock: \nhttps://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
            openPage()
            notif(mail_content)                
            while i == 1:
                try:
                    status = webAccess()
                    if status != 'Sold Out':
                        nothing = 0
                    else:
                        break
                except:
                    nothing = 0

        elif status == 'Sold Out':
            mail_content = "The Product is Sold Out!"
            openPage()
            notif(mail_content)
            while i == 1:
                try:
                    status = webAccess()
                    if status == 'Sold Out':
                        nothing = 0
                    else:
                        break
                except:
                    nothing = 0
    except:
        nothing = 0