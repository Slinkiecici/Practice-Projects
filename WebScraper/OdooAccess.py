import odoolib
import xmlrpc.client
from xmlrpc import client as xmlrpclib

f = open('WebScraper/odoocredentials.txt', 'r')                     #retreive log in details from seperate txt file
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
print (models.execute_kw(
    db, uid, password, 'product.product', 'search_read',
    [], {'fields': ['code','price', 'qty_available']}))

