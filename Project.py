from urllib import request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

from twilio.rest import Client

accountSID = 'AC00618327f5be709106f07f22fcce4b5f'

authToken = '5cca88682d5e1d961e63b6c4ce35bb90'

TwilioNumber = '+18053011466'

myphone = '+17139095350'

client = Client(accountSID,authToken)

url = 'https://www.cryptoslate.com/coins/'
headers = headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

#print(title.text)

table_rows = soup.findAll("tr")

for row in table_rows[1:6]:
    td = row.findAll("td")
    id = td[2].text.split(" ")
    name = id[0]
    sym = id[1]
    price = td[4].text
    change = td[5].text
    print("Name:", name)
    print("Symbol:", sym)
    print("Price:", price)
    print("24 Hr % Change:", change)

    act_price = td[4].text.replace(",","").replace("$","")
    act_price = float(act_price)
    perchange = float(change.replace("%","e-2"))

    checker = "+"
    if checker in change:
        corr = (act_price * perchange) + act_price
    else:
        corr = act_price - (act_price * perchange)

    for_corr = "${:,.2f}".format(corr)
    print("Corresonding Change Price:", for_corr)

    if name == "Bitcoin":
        bcp = act_price
        if bcp < 40000:
            textmessage = client.messages.create(to=myphone,from_=TwilioNumber,body="Bitcoin(BTC) is below $40,000")
    
    if name == "Ethereum":
        ep = act_price
        if ep < 3000:
            textmessage = client.messages.create(to=myphone,from_=TwilioNumber,body="Ethereum(ETH) is below $3,000")
    
    input()
