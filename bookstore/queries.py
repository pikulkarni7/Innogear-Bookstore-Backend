from django.db import connection
 
 

def make_par(value):
    return "'"+str(value)+"'"
 

def addCustomer(id, type, email, address, name):
    with connection.cursor() as cursor:
        sql_str = 'INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name) VALUES' + ' (' +  str(id) + ',' + make_par(type) + ',' + make_par(email) + ',' + make_par(address) + ',' + make_par(name) + ')' + ';'
        print(sql_str)
        cursor.execute(sql_str)       
    return None


def createCustomerOrder(customerid):
    with connection.cursor() as cursor:
        order_id = cursor.callfunc('CustOrder', int, [customerid])
        print(order_id)
        return order_id


def createOrderLineItem(itemid, orderid, copies_ordered):
    with connection.cursor() as cursor:       
        cursor.callproc('createOrderLineItem', [itemid, orderid, copies_ordered])
    return None


def computeTotal(orderid):
    with connection.cursor() as cursor:       
        total = cursor.callfunc('computeTotal', float, [orderid])        
    return total
        




