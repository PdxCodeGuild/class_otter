# Utilities for Urlshortener
from django.conf import settings

from random import choice

from string import ascii_letters, digits

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7) # Allows for adjustability: First it looks for the value in the settings module
                                                 # 'settings.py' or it defaults to '7'.  It will then return a random string the 
                                                 # length equal to what's in 'settings.py, or the default set to '7.'                                    
                                                 # using the function 'getattr' gets a variable without throwing an error if the 
                                                 # variable isn’t specified.

AVAIABLE_CHARS = ascii_letters + digits 


def create_random_code(chars=AVAIABLE_CHARS): # Creates a random string with the predetermined 'SIZE'
    return "".join(
        [choice(chars) for _ in range(SIZE)] # loops - generate random characters equal to the length of the predetermined 'SIZE'
    )
    
def create_shortened_url(model_instance):
    random_code = create_random_code() #calls function to get a random code
    model_class = model_instance.__class__  # sets model class equal to model_instance.the class from which the object was created (in this case Urlshort)

    if model_class.objects.filter(short_url=random_code).exists(): #checks if short_url is unique.  
                                                                   # If unique, it returns the new shortened URL,
                                                                   # If it is not unique, it regenerates the random and 
                                                                   # loops until it is unique.
        return create_shortened_url(model_instance) # returns the new shortened URL

    return random_code # Loop run the function again