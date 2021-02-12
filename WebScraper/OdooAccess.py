import odoolib
import xmlrpc.client
from xmlrpc import client as xmlrpclib

f = open('odooCredentials.txt', 'r')                     #retreive log in details from seperate txt file
content = f.read().split()                              #split value at new line to give two seperate variables
url = content[0]
db= content[1]
username = content[2]
password = content[3]

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()
{
    "server_version": "13.0",
    "server_version_info": [13, 0, 0, "final", 0],
    "server_serie": "13.0",
    "protocol_version": 1,
}

uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
product_details =  (models.execute_kw(
             db, uid, password, 'product.product', 'search_read',
             [],{'fields': ['display_name','code', 'qty_available']}  ))

 #{'fields': ['product_variant_ids','is_product_variant', 'qty_available']}  {'fields': ['code','product_variant_id']}
def Show_all_in_stock():
    product_details =  (models.execute_kw(
             db, uid, password, 'product.product', 'search_read',
             [],{'fields': ['display_name','code', 'qty_available']}  ))
    for product in product_details:
        for key,value in product.items():
                if key == "qty_available" and value > 0.0:
                    print (product)

def display_specific_product(product_name):
    product_details =  (models.execute_kw(
             db, uid, password, 'product.product', 'search_read',
             [],))
    product_search = product_name
    for product in product_details:
        for key,value in product.items():
            if key == "product_variant_id":
                if str(product_search).capitalize() in str(value).capitalize():
                    print (product)
                else: continue

def display_all():
    product_details =  (models.execute_kw(
            db, uid, password, 'product.product', 'search_read',
            [], ))
    for product in product_details:
        print (product)


def test_create_quant_3():
    """ Try to create a quant with `inventory_quantity` but not in inventory mode.
    Creates two quants not in inventory mode:
        - One with `quantity` (this one must be OK)
        - One with `inventory_quantity` (this one must be null)
    """
    valid_quant = env['stock.quant'].create({
        'product_id': 21,
        'location_id': 8,
        'quantity': 100,
    })
    invalid_quant = env['stock.quant'].create({
        'product_id': 21,
        'location_id': 8,
        'inventory_quantity': 200,
    })
    self.assertEqual(valid_quant.quantity, 100)
    self.assertEqual(invalid_quant.quantity, 0)


def update_stock_value():
    models.execute_kw(db, uid, password, 'stock.quant', 'write', [[225], {
        'inventory_quantity' : float(123.0),
    }])


#update_stock_value()
#display_specific_product("tester")
#display_all()
#Show_all_in_stock()
test_create_quant_3()

product_quantity = (models.execute_kw(db, uid, password, 'stock.quant', 'search_read',
            [], ))

#for product in product_quantity:
#    print (product)
