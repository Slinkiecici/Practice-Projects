import odoolib
import xmlrpc.client
from xmlrpc import client as xmlrpclib

class OdooActions :
    def __init__(self):
        f = open('odooCredentials.txt', 'r')                     #retreive log in details from seperate txt file
        content = f.read().split()                              #split value at new line to give two seperate variables
        self.url = content[0]
        self.db= content[1]
        self.username = content[2]
        self.password = content[3]
        self.product_details = {}
        self.product_spec = []
        self.all_product_details = {}
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        common.version()
        {
            "server_version": "13.0",
            "server_version_info": [13, 0, 0, "final", 0],
            "server_serie": "13.0",
            "protocol_version": 1,
        }
        self.uid = common.authenticate(self.db, self.username, self.password, {})
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

 
    def Show_all_in_stock(self):
        self.product_details =  (self.models.execute_kw(
                self.db, self.uid, self.password, 'product.product', 'search_read',
                [],{'fields': ['code', 'qty_available', 'description']}  ))
        return self.product_details


    def display_specific_product(self, product_name):
        product_details =  (self.models.execute_kw(
                self.db, self.uid, self.password, 'product.product', 'search_read',
                [], ))
        product_search = product_name
        for product in product_details:
            for key,value in product.items():
                if key == "product_variant_id":
                    if str(product_search).capitalize() in str(value).capitalize():
                        self.product_spec.append(product)
                    else: continue
        return (self.product_spec)

    def display_all(self):
        self.all_product_details =  (self.models.execute_kw(
                self.db, self.uid, self.password, 'product.product', 'search_read',
                [],{'fields': ['code', 'qty_available', 'description']} ))
        return (self.all_product_details)


    def update_stock_value(self): #THis function does naaaaaaaaaaaaaaat work yet.
        self.models.execute_kw(db, self.uid, self.password, 'stock.quant', 'write', [[225], {
            'inventory_quantity' : float(123.0),
        }])
        product_quantity = (self.models.execute_kw(self.db, self.uid, self.password, 'stock.quant', 'write', [[165], {
            'inventory_quantity' : float(0.0),
            'quantity' : float(123.0),
            'available_quantity' : float(123.0),
            'reserved_quantity' : float(123.0),
        }]))

odoo_action = OdooActions()
#update_stock_value()
#display_specific_product("tester")
#odoo_action.display_all()
#Show_all_in_stock()
#test_create_quant_3()
