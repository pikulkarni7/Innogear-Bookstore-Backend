from django.db import connection
 
 

def make_par(value):
    return "'"+str(value)+"'"
 
 

def addCustomer(id, type, email, address, name):
    with connection.cursor() as cursor:
        sql_str = 'INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name) VALUES' + ' (' +  str(id) + ',' + make_par(type) + ',' + make_par(email) + ',' + make_par(address) + ',' + make_par(name) + ')' + ';'
        print(sql_str)
        cursor.execute(sql_str)
       
    return None



def createOrderLineItem(itemid, customerid, copies_ordered):
    with connection.cursor() as cursor:       
        message = cursor.callproc('createOrderLineItem', [itemid, customerid, copies_ordered])
    
    return message


def computeTotal(orderid):
    with connection.cursor() as cursor:       
        total = cursor.callfunc('computeTotal', float, [orderid])
        
    return total
        




