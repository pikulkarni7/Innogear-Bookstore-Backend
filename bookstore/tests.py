from django.test import TestCase
from .queries import add_customers

# Create your tests here.
class BookStoreTest(TestCase):
    
    def test_add_customers():
        
        add_customers()
        assert 1 == 1