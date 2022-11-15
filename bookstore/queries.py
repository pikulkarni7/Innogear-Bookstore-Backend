from django.db import connection
 
 

def make_par(value):
    return "'"+str(value)+"'"
 
def addCustomer(id, type, email, address, name):
    with connection.cursor() as cursor:
        sql_str = 'INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name) VALUES' + ' (' +  str(id) + ',' + make_par(type) + ',' + make_par(email) + ',' + make_par(address) + ',' + make_par(name) + ')' + ';'
        print(sql_str)
        cursor.execute(sql_str)
       
    return None 



def createCustOrder(self):
    with connection.cursor() as cursor:
        cursor.execute("")
    
    return None

