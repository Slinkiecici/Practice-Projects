from grab import Grab                   #first version 0.6.41 used
from bs4 import BeautifulSoup as bs     #first version 4.93 used
import mammoth                          #first version 1.4.15 used
import os

class SiteActions :
    def __init__(self):
        pass
    def LoginSite (self):
        f = open('WebScraper/credentials.txt', 'r')             #retreive log in details from seperate txt file
        content = f.read().split()                              #split value at new line to give two seperate variables
        login_name = content[0]
        login_password = content[1]

        #accessing webpage via Grab framework
        g = Grab()
        g.setup(connect_timeout=5, timeout=5)
        g.go("https://mall.industry.siemens.com/regpublic/Login.aspx?regionkey=ZA&lang=en&app=MALL&ret=https%3a%2f%2fmall.industry.siemens.com%2fgoos%2fWelcomePage.aspx%3fregionUrl%3d%252fza")
        g.doc.set_input("ctl00$ContentPlaceHolder1$TextSiemensLogin", login_name )          #id used on page for input field of login name
        g.doc.set_input("ctl00$ContentPlaceHolder1$TextPassword", login_password)           #id used on page for input field of password
        g.submit()                                                                          #submits form to login

        response = g.go('https://mall.industry.siemens.com/mall/za/za/Catalog/Product/6ES7332-5HD01-0AB0')

        #writing grab.document file to html file to be used by beautiful soup
        f = open("WebScraper/file.html", "w")
        new_response = (response.body)
        new_response =  (new_response.decode("utf-8"))
        new_response = str(new_response)
        f.write(new_response)
        f.close()

    def ExctractInfo (self, file_name):
        #Reading html file with beautiful soup and extracting price
        with open(file_name) as fp:
            soup = bs(fp, 'lxml')
            list_price = soup.find("td" ,{"id" : "ListPriceCell"}).text
            customer_price = soup.find("td" ,{"id" : "CustomerPriceCell"}).text
            print (list_price, customer_price)

site_action = SiteActions()
site_action.ExctractInfo('WebScraper/file.html')




