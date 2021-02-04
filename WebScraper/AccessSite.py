from grab import Grab
from bs4 import BeautifulSoup as bs
import mammoth
import os

f = open('WebScraper/credentials.txt', 'r')             #retreive log in details from seperate txt file
content = f.read().split()
login_name = content[0]
login_password = content[1]

#accessing webpage via Grab framework
g = Grab()
g.setup(connect_timeout=5, timeout=5)
g.go("https://mall.industry.siemens.com/regpublic/Login.aspx?regionkey=ZA&lang=en&app=MALL&ret=https%3a%2f%2fmall.industry.siemens.com%2fgoos%2fWelcomePage.aspx%3fregionUrl%3d%252fza")
g.doc.set_input("ctl00$ContentPlaceHolder1$TextSiemensLogin", login_name )
g.doc.set_input("ctl00$ContentPlaceHolder1$TextPassword", login_password)
g.submit()

response = g.go('https://mall.industry.siemens.com/mall/za/za/Catalog/Product/6ES7332-5HD01-0AB0')

#writing grab.document file to html file to be used by beautiful soup
f = open("WebScraper/file.html", "w")
new_response = (response.body)
new_response =  (new_response.decode("utf-8"))
new_response = str(new_response)
f.write(new_response)
f.close()

#Reading html file with beautiful soup and extracting price
with open('WebScraper/file.html') as fp:
    soup = bs(fp, 'lxml')
    list_price = soup.find("td" ,{"id" : "ListPriceCell"}).text
    customer_price = soup.find("td" ,{"id" : "CustomerPriceCell"}).text
    print (list_price, customer_price)

