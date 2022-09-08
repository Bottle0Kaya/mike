from django import forms
from django.forms import ModelForm
from .models import Venue, plant_inf

class plant_infoForm(ModelForm):
    class Meta:
        model= plant_inf
        fields =('Plant_name', 'Color', 'Plant_type', 'Origin')
        labels ={
            'Plant_name': '',
            'Color': '',
            "Plant_type": '',
            "Origin": '',
        }
        widgets = {
            'Plant_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Plant Name'}),
            'Color': forms.TextInput(attrs={'class':'form-control',  'placeholder':'Color'}),
            "Plant_type": forms.TextInput(attrs={'class':'form-control',  'placeholder':'Plant Type'}),
            "Origin": forms.TextInput(attrs={'class':'form-control',  'placeholder':'Origin'}),
        }



class VenueForm(ModelForm):
    class Meta:
        model= Venue
        fields =('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels ={
            'name': '',
            'address': '',
            "zip_code": '',
            "phone": '',
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
            'address': forms.TextInput(attrs={'class':'form-control',  'placeholder':'Address'}),
            "zip_code": forms.TextInput(attrs={'class':'form-control',  'placeholder':'Zip Code'}),
            "phone": forms.TextInput(attrs={'class':'form-control',  'placeholder':'Phone'}),
            'web': forms.TextInput(attrs={'class':'form-control' ,  'placeholder':'Web Address'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control',  'placeholder':'Email Address'}),
        }