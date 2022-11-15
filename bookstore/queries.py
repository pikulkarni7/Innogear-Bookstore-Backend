from django.db import connection
 
 
def add_customers(self):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name) VALUES (2, ‘R’, 'shreya@scu.edu', 'San Mateo', 'Shreya');")
        cursor.execute("INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name, coupon, date_joined) VALUES (3, ‘G’, 'yashom@scu.edu',' Santa Clara', 'Yashom',' Y123', '11-NOV-22');")
        cursor.execute("INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name) VALUES (4, ‘R’, 'riya@scu.edu', 'San Jose', 'Riya');")
        cursor.execute("INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name) VALUES (5, ‘R’, 'prem@scu.edu', 'San Jose', 'Prem');")
        cursor.execute("INSERT INTO BOOKSTORE_GOLDCUSTOMER (id, type, email_id, address, name) VALUES (6, ‘G’, 'anjali@scu.edu', 'San Jose', 'Anjali', 'A234', '01-JAN-22');")
        cursor.execute("INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name) VALUES (7, ‘R’, 'dan@scu.edu', 'San Jose', 'Dan');")
        cursor.execute("INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name) VALUES (8, ‘R’, 'priya@scu.edu',' San Jose', 'Priya');")
        cursor.execute("INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name) VALUES (9, ‘R’,' mridul@scu.edu', 'San Jose', 'Mridul');")
        cursor.execute("INSERT INTO BOOKSTORE_CUSTOMER (id, type, email_id, address, name) VALUES (10, ‘G’, 'jan@scu.edu','San Jose', 'Jane', 'J786',' 21-SEPT-99');")

        print(cursor.fetchall())
        
    return None 



def createCustOrder(self):
    with connection.cursor() as cursor:
        cursor.execute("")
    
    return None