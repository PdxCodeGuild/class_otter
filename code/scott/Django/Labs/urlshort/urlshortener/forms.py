'''
URLshortener forms urlshortener/forms.py
'''

from django import forms

from .models import Urlshort

class ShortenerForm(forms.ModelForm): #a model form to create a model object from the user input.
                                      # 'widget' argument specifies the class attribute for CSS style sheet 
    
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "The URL to shorten"}))
    
    class Meta:
        model = Urlshort

        fields = ('long_url',)