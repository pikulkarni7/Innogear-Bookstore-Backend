from django.test import TestCase
from .queries import addCustomer

# Create your tests here.
class BookStoreTest(TestCase):
    
    def test_add_customers():
        
        addCustomer(id=567, type='R', email='airpods@apple.com', address='San Jose', name='Anish Kulkarni')
        assert 1 == 1