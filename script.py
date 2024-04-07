from bs4 import BeautifulSoup
import smtplib, ssl, base64, requests, json

with open("config.json", 'r') as f:
    config = json.loads(f.read())
with open("mailbody.txt", "r") as m:
    body = m.read()

URL = config["URL"]
ServerEmail = config["ServerEmail"]
sendlist = config["SendList"]
port = config["port"]
secret = config["AuthSecret"]

context = ssl.create_default_context()

def scrape():
    global JackpotAmount
    Webpage = BeautifulSoup(requests.get(URL).content, "html.parser")
    result = str(Webpage.find_all(attrs={'class': 'jackcurr'}))
    JackpotAmount = int(''.join(x for x in result if x.isdigit()))
def SendAlert():
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(ServerEmail,base64.b64decode(secret).decode("utf-8"))
        server.sendmail(ServerEmail,sendlist,body)
def Main():
    scrape()
    if JackpotAmount == 120:
        SendAlert()

    else:
        exit()

Main()
