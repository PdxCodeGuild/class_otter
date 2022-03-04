'''
URLshortener Forms urlshortener/forms.py
'''

from django import forms

from .models import Urlshort

class ShortenerForm(forms.ModelForm):
    
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))
    
    class Meta:
        model = Urlshort

        fields = ('long_url',)