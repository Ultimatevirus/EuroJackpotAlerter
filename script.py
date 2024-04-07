""" Simple script to send an alert if eurojackpot has reached it's max jackpot """
import sys
import smtplib
import ssl
import base64
import json
import requests
from bs4 import BeautifulSoup

with open("config.json", 'r', encoding="utf8") as f:
    config = json.loads(f.read())


def scrape():
    """Scrape webpage, find eurojackpot size and returns amount"""
    url = config["URL"]
    webp = BeautifulSoup(requests.get(url, timeout=10).content, "html.parser")
    jack = str(webp.find_all(attrs={'class': 'jackcurr'}))
    jackpot_amount = int(''.join(x for x in jack if x.isdigit()))
    return jackpot_amount


def netamountline(jackpot_amount):
    """calculates net winnings and creates a string"""
    net = str(float(config["TaxFactor"]) * jackpot_amount)
    net_amount_line = " After taxes, you'd win: " + net + " million euros"
    return net_amount_line


def sendalert(jackpot_amount):
    """Function sends email through gmail SMTP with settings from config, with body.txt """
    with open("mailbody.txt", 'r', encoding="utf8") as m:
        body = m.read()

    context = ssl.create_default_context()
    serveremail = config["ServerEmail"]
    with smtplib.SMTP_SSL(config["SMTP"], config["port"], context=context) as server:
        server.login(serveremail,base64.b64decode(config["AuthSecret"]).decode("utf-8"))
        server.sendmail(serveremail,config["SendList"],body + netamountline(jackpot_amount))


def main():
    """Simple if statement so an alert is only sent if the jackpot is at it's maximum"""
    jackpot_amount = scrape()
    if jackpot_amount == 120:
        sendalert(jackpot_amount)
    else:
        sys.exit(0)


main()
