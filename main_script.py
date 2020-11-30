#!/usr/bin/env python3
# v 1.1.0
import sys
import os
import requests
import time
from bs4 import BeautifulSoup
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
import xmpp
import config as cfg
import argparse

cfg.keywords += ["out of stock", "OUT OF STOCK", "Out of Stock", "Out of stock", "Temporarily unavailable"]

parser = argparse.ArgumentParser(description='An inventory checking message bot')
parser.add_argument('-d','--desktop', help='Display libnotify messages', action='store_true')
args = parser.parse_args()

if (args.desktop):
    import subprocess as s
    
def send_email ( message ):
    msg = MIMEText(message, 'plain')
    msg['To'] = cfg.email["toaddr"]
    msg['Subject'] = "Product Stock Alert!"
    server = SMTP( cfg.email["server"] )
    server.login( cfg.email["fromaddr"], cfg.email["password"] )
    server.sendmail(cfg.email["fromaddr"], cfg.email["toaddr"], msg.as_string())
    server.quit()

def send_xmpp( message ):
    jid = xmpp.protocol.JID(cfg.xmpp["jabberid"])
    connection = xmpp.Client(server=jid.getDomain(), debug=[])
    connection.connect()
    connection.auth(user=jid.getNode(), password=cfg.xmpp["password"], resource=jid.getResource())
    connection.send(xmpp.protocol.Message(to=cfg.xmpp["recipient"], body=message, typ="chat"))
    
found = 0

# cycle through the product page url list
for url in cfg.urls:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    # cycle through the keywords for each product page, stopping when one is found
    for keyword in cfg.keywords:
        if str(soup).find( keyword ) != -1:
            break
    # no errors were found, send the alert
    else:
        found += 1
        title = soup.find('title')
        message = 'Now In Stock:\n\n"'+title.string+'"\n\n' + url
        
        if (args.desktop):
        	s.call(['notify-send','Stock Check:', message ])
        	
        if cfg.protocol == "email":
            send_email( message )
        elif cfg.protocol == "xmpp":
            send_xmpp( message )
        elif cfg.protocol == "both":
            send_email( message )
            send_xmpp( message )

if (args.desktop):
    if found == 0:
	    s.call(['notify-send','Stock Check:','No luck!'])
