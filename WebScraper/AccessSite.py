from grab import Grab                   #first version 0.6.41 used
from bs4 import BeautifulSoup as bs     #first version 4.93 used
import mammoth                          #first version 1.4.15 used
import os
import pandas as pd


class SiteActions :
    def __init__(self):
        self.parts_list = []                                        #list created in  compile_list_to_scrape and contains part numbers from an input excel sheet downloaded from odoo
        self.excel_format = []                                      #list containing product and product info to be written to excel used in write_to_excel
        self.failed = []                                            #shows failed product codes, intention is to display to user to edit and rerun scraper

    def login_site (self):
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
        g.setup(connect_timeout=6, timeout=6)
        #print (g.doc.body)
        for part in self.parts_list:
            if (len(str(part))) < 5:
                pass
            else:
                try: 
                    response = g.go('https://mall.industry.siemens.com/mall/en/za/Catalog/Product/' +str(part))         #url to load by concatenating base url with part name
                    #writing grab.document file to html file to be used by beautiful soup
                    f = open("WebScraper/file.html", "w")                                                               #temporary file to read html data from
                    new_response = (response.body)
                    new_response =  (new_response.decode("utf-8"))
                    new_response = str(new_response)
                    f.write(new_response)
                    f.close()
                    try:
                        self.extract_info("WebScraper/file.html")                                                       #passing temporary html file to extract_info function to pull relevant data
                    except:
                        self.failed.append(str(part))                                                     
                except: 
                    self.failed.append(str('https://mall.industry.siemens.com/mall/en/za/Catalog/Product/' +str(part)))     #if unable to correctly load page, add to failed list to be displayed
    def extract_info (self, file_name):
        #Reading html file with beautiful soup and extracting price
        with open(file_name) as fp:
            soup = bs(fp, 'lxml')                                                                                           #Using beautiful soup to pull values from html using element id and class

            list_price = soup.find("td" ,{"id" : "ListPriceCell"}).text.strip()
            customer_price = soup.find("td" ,{"id" : "CustomerPriceCell"}).text.strip()
            product_description = soup.find("div", {"class": "productdescription"}).text.strip()
            product_code = soup.find("span", {"class": "productIdentifier"}).text.strip()
            product_list = ((product_code, product_description, list_price, customer_price))                            #Create a list of one product info to be appenended to larger list
            self.excel_format.append(product_list)
            return self.excel_format
                                                                                                       
             

    
    def write_to_excel (self):
        df1 = pd.DataFrame(self.excel_format)                                                                               #converts list with strings in to a dataframe to be used by panda framework
        df1.drop_duplicates()                                                                                               #Drops any instances of duplication if they made it through
        df1.columns = ["Product code", "Description", "List Price", "Customer Price"]
        df1.to_excel('WebScraper/UpdatedSiemensPriceList.xlsx')                                                             #Writes dataframe to excel sheet
        print (df1)
    
    def compile_list_for_scrape (self):                                                 
        df = pd.read_excel (r'WebScraper/product.product.xlsx')                                                             #Reads values from odoo exported prodct list
        self.parts_list = df['Internal Reference'].tolist()                                                                 #Odoo labels parts list as Internal Reference
        self.parts_list = list(dict.fromkeys(self.parts_list))                                                              #converts list to dictionary to drop duplicates then back to list





site_action = SiteActions()
site_action.compile_list_for_scrape()
site_action.login_site()
site_action.write_to_excel()
print (site_action.failed)




