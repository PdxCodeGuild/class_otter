# ***************************************************** #
#                  copy_pad_20220126.py                 #
#   requests exceptions errors response get HTTPError   #
#                      Version: 0.0                     #
#                  Author: Bruce Stull                  #
#                       2022-01-26                      #
# ***************************************************** #

# import requests module
import requests

# #############################
# # This works as expected
# #############################
# # Making a get request
# print(f"Make request get...")
# response = requests.get('https://api.github.com/')

# # print response
# print(f"The response of 'requests.get('https://api.github.com/')': {response}")

# # print check if an error has occurred
# raise_for_status_response = response.raise_for_status()
# print(f"raise_for_status_response: {raise_for_status_response}")
# print(f"Done!")

# # Make request get...
# # The response of 'requests.get('https://api.github.com/')': <Response [200]>
# # raise_for_status_response: None
# # Done!
# #############################


# #############################
# # This doesn't work. A space in the url.
# #############################
# # ping an incorrect url
# print(f"Trying incorrect url...")
# response = requests.get('https://geeksforgeeks.org / naveen/')
# print(f"Incorrect url done!")

# # print check if an error has occurred
# raise_for_status_response = response.raise_for_status()
# print(f"raise_for_status_response: {raise_for_status_response}")
# #############################


# ############################
# # Example error handling from else-where.
# # https://stackoverflow.com/a/70517735
# ############################
# url = 'https://api.github.com/'
# print("Try...")
# try:
#     r = requests.get(url)

#     # process the specific codes from the range 400-599
#     # that you are interested in first
#     if r.status_code == 400:
#         invalid_request_reason = r.text
#         print(f"Your request has failed because: {invalid_request_reason}")
#     # this will handle all other errors
#     elif r.status_code > 400:
#         print(f"Your request has failed with status code: {r.status_code}")

# except requests.exceptions.ConnectionError as err:
#     # eg, no internet
#     raise SystemExit(err)

# print("Done!!")

# # Try...
# # Done!!
# ############################


# # Add some type of error and then figure out how to catch it.
# ############################
# # Example error handling from else-where.
# # https://stackoverflow.com/a/70517735
# ############################
# url = 'https://api.github.com/'
# print("Try...")
# try:
#     r = requests.get(url)

#     # process the specific codes from the range 400-599
#     # that you are interested in first
#     if r.status_code == 400:
#         invalid_request_reason = r.text
#         print(f"Your request has failed because: {invalid_request_reason}")
#     # this will handle all other errors
#     elif r.status_code > 400:
#         print(f"Your request has failed with status code: {r.status_code}")

# except requests.exceptions.ConnectionError as err:
#     # eg, no internet
#     raise SystemExit(err)

# print("Done!!")

# # Try...
# # Done!!
# ############################



# #############################
# # Try to catch the exception
# #############################

# # # Incorrect url:
# # url = 'https://geeksforgeeks.org / naveen/'
# # # requests.exceptions.ConnectionError: HTTPSConnectionPool(host='geeksforgeeks.org%20', port=443): Max retries exceeded with url: /%20naveen/ 

# # # Let's try to catch this exception.
# # # Correct url:
# # url = 'https://geeksforgeeks.org/naveen/'
# # # Trying url...
# # # Done!
# # # Traceback (most recent call last):
# # #   File "C:\Users\Bruce\Programming\class_otter\code\bruce\other_code\copy_pad\week_04\copy_pad_20220126.py", line 122, in <module>
# # #     raise_for_status_response = response.raise_for_status()
# # #   File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\models.py", line 960, in raise_for_status
# # #     raise HTTPError(http_error_msg, response=self)
# # # requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://www.geeksforgeeks.org/naveen/

# # My github url
# url = 'https://github.com/brucestull'
# # Trying url...
# # Done!
# # raise_for_status_response: None

# # ping a url
# print(f"Trying url...")
# response = requests.get(url)
# print(f"Done!")

# # print check if an error has occurred
# raise_for_status_response = response.raise_for_status()
# print(f"raise_for_status_response: {raise_for_status_response}")
# #############################


# #############################
# # Try to catch the exception
# #############################

# # Let's try to catch this exception.
# # Correct url:
# url = 'https://geeksforgeeks.org/naveen/'
# # Trying url...
# # Done!
# # Traceback (most recent call last):
# #   File "C:\Users\Bruce\Programming\class_otter\code\bruce\other_code\copy_pad\week_04\copy_pad_20220126.py", line 122, in <module>
# #     raise_for_status_response = response.raise_for_status()
# #   File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\models.py", line 960, in raise_for_status
# #     raise HTTPError(http_error_msg, response=self)
# # requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://www.geeksforgeeks.org/naveen/
# try:
#     # ping a url
#     print(f"Trying url...")
#     response = requests.get(url)
#     print(f"Done!")

#     # print check if an error has occurred
#     raise_for_status_response = response.raise_for_status()
#     print(f"raise_for_status_response: {raise_for_status_response}")
# except requests.exceptions.HTTPError as requests_exceptions_HTTPError:
#     print(f"type(requests_exceptions_HTTPError): {type(requests_exceptions_HTTPError)}")
#     print(requests_exceptions_HTTPError)

# # Trying url...
# # Done!
# # type(requests_exceptions_HTTPError): <class 'requests.exceptions.HTTPError'>
# # 404 Client Error: Not Found for url: https://www.geeksforgeeks.org/naveen/

# # NOTE:

# # Previous result (Traceback shown):
# # Traceback (most recent call last):
# #   File "C:\Users\Bruce\Programming\class_otter\code\bruce\other_code\copy_pad\week_04\copy_pad_20220126.py", line 122, in <module>
# #     raise_for_status_response = response.raise_for_status()
# #   File "C:\Users\Bruce\AppData\Local\Programs\Python\Python310\lib\site-packages\requests\models.py", line 960, in raise_for_status
# #     raise HTTPError(http_error_msg, response=self)
# # requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://www.geeksforgeeks.org/naveen/

# # New result (Traceback not shown):
# # Trying url...
# # Done!
# # 404 Client Error: Not Found for url: https://www.geeksforgeeks.org/naveen/
# #############################



#############################
# Add a space within url to see if this exception can be caught.
#############################

# "Done!" is being printed but not f"raise_for_status_response: {raise_for_status_response}".
# Why is that?
url = 'https://geeksforgeeks.org/ naveen/'

try:
    print(f"Trying url...")
    # Trying url...
    response = requests.get(url)
    print(f"Done!")
    # Done!

    print("Just before response.raise_for_status()")
    # Just before response.raise_for_status()
    raise_for_status_response = response.raise_for_status()  # Nothing appears after this line until the 'except'.
    print("Just after response.raise_for_status()")
    print(type(response.raise_for_status()))
except requests.exceptions.HTTPError as requests_exceptions_HTTPError:  # This line creates 'requests_exceptions_HTTPError', which is displayed below.
    # print(f"raise_for_status_response: {raise_for_status_response}")  # 'NameError: name 'raise_for_status_response' is not defined' # NOTE: This line causes NameError.
    print(f"type(requests_exceptions_HTTPError): {type(requests_exceptions_HTTPError)}")
    # type(requests_exceptions_HTTPError): <class 'requests.exceptions.HTTPError'>
    print(requests_exceptions_HTTPError)
    # 404 Client Error: Not Found for url: https://www.geeksforgeeks.org/%20naveen/

# Putting a space ' ' in an incorrect position results in:
# Trying url...
# Done!
# type(requests_exceptions_HTTPError): <class 'requests.exceptions.HTTPError'>
# 404 Client Error: Not Found for url: https://www.geeksforgeeks.org/%20naveen/
#############################