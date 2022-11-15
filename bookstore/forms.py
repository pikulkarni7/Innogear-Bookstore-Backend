from django import forms
from . import models


class CreateCustomer(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['id', 'name', 'type', 'email_id', 'address']
        
