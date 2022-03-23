# *************************** #
#        HTTP Requests        #
#   Uses 'requests' library   #
#         Version: 0.0        #
#     Author: Bruce Stull     #
#          2022-01-17         #
# *************************** #

import requests
from requests.exceptions import HTTPError
import json

# Resources:
# https://github.com/brucestull/PDX_Full_Stack/blob/bruce/1%20Python/docs/15%20Requests.md

# Needed to install requests
# In terminal:
    # pip install requests


def print_variable_and_description(variable_under_review, description_of_logic = '', print_logic_results = True):
    '''Accepts three arguments: A variable we are examining, a description of the logic we are examining, and a print flag.'''
    __name__ = print_variable_and_description
    string_result = f"{print_variable_and_description.__name__}: {description_of_logic}: {variable_under_review}"
    if print_logic_results:
        print(string_result)


# ############# Request without params ################
# # We get an object and call it 'response'. We can retrieve all manner of data using the different variables ('url', 'text', etc) on the 'response' object.
# response = requests.get('https://api.ipify.org')

# print(f"response: {response}")  # <Response [200]>
# print(f"type(response): {type(response)}")  # <class 'requests.models.Response'>
# print(f"response.url: {response.url}")  # https://api.ipify.org/
# print(f"response.text: {response.text}") # 75.179.180.20
# print(f"response.status_code: {response.status_code}") # 200
# print(f"respong.encoding: {response.encoding}") # ISO-8859-11
# print(f"response.headers: {response.headers}")  # {'Server': 'Cowboy', 'Connection': 'keep-alive', 'Content-Type': 'text/plain', 'Vary': 'Origin', 'Date': 'Mon, 17 Jan 2022 22:22:47 GMT', 'Content-Length': '13', 'Via': '1.1 vegur'}

# # response: <Response [200]>
# # type(response): <class 'requests.models.Response'>
# # response.url: https://api.ipify.org/
# # response.text: 75.179.180.20
# # response.status_code: 200
# # respong.encoding: ISO-8859-1
# # response.headers: {'Server': 'Cowboy', 'Connection': 'keep-alive', 'Content-Type': 'text/plain', 'Vary': 'Origin', 'Date': 'Sat, 22 Jan 2022 14:11:09 GMT', 'Content-Length': '13', 'Via': '1.1 vegur'}
# #####################################################


# ########### Request with params ###########
# # Here, we are requesting the return formatted in json.
# # NOTE: It seems that response[url,text,encoding] return different values than above request, which is without specified parameters.
# response = requests.get('https://api.ipify.org', params={'format': 'json'})

# print(f"response: {response}")
# print(f"type(response): {type(response)}")
# print(f"response.url: {response.url}")  # response.url: https://api.ipify.org/?format=json
# print(f"response.text: {response.text}")    # response.text: {"ip":"75.179.180.20"}
# print(f"response.status_code: {response.status_code}")
# print(f"respong.encoding: {response.encoding}") # respong.encoding: utf-8
# print(f"response.headers: {response.headers}")

# # response: <Response [200]>
# # type(response): <class 'requests.models.Response'>
# # response.url: https://api.ipify.org/?format=json
# # response.text: {"ip":"75.179.180.20"}
# # response.status_code: 200
# # respong.encoding: utf-8
# # response.headers: {'Server': 'Cowboy', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Vary': 'Origin', 'Date': 'Sat, 22 Jan 2022 14:39:49 GMT', 'Content-Length': '22', 'Via': '1.1 vegur'}
# ###########################################

# If the response is in JSON, you can turn it into a python dictionary using the json.loads() function
# or the json() method on the response object. You can then extract the relevant data.

# ################### Using json.loads() funcion or json() method #################
# response = requests.get('https://api.ipify.org', params={'format': 'json'})

# print(f"response: {response}")  # response: <Response [200]>
# print(f"response.text: {response.text}")    # response.text: {"ip":"75.179.180.20"}

# data = response.json() # turn raw json into a python dictionary
# print(f"data: {data}")
# print(f"data['ip']: {data['ip']}")
# print(response.headers['Date'])

# # data: {'ip': '75.179.180.20'}
# # data['ip']: 75.179.180.20
# # Sat, 22 Jan 2022 17:29:19 GMT

# data = json.loads(response.text) # use the json library to parse the raw response
# print(f"data: {data}")
# print(f"data['ip']: {data['ip']}")
# print(response.headers['Date'])

# # data: {'ip': '75.179.180.20'}
# # data['ip']: 75.179.180.20
# # Sat, 22 Jan 2022 17:29:19 GMT

#################################################################################

# ##############################################################################
# # View json key/value pairs.
# response = requests.get('https://api.ipify.org', params={'format': 'json'})

# response = response.json() # turn raw json into a python dictionary

# print(f"response: {response}")  # response: {'ip': '75.179.180.20'}

# the_keys = response.keys()
# print(f"the_keys: {the_keys}")  # the_keys: dict_keys(['ip'])

# # Let's print out the key:value pairs of the 'response' object.
# # NOTE: This particular response object only has one entry/element/pair.
# print("Print key:value pairs from 'response' object.")
# for key, value in response.items():
#     print(f"{key} : {value}")

# # Print key:value pairs from 'response' object.
# # ip : 75.179.180.20
# ##############################################################################

#################################################################################
# Get a response which has more elements.

# May need to include some error handling.
# https://pynative.com/parse-json-response-using-python-requests-library/

try:
    response = requests.get('https://httpbin.org/get')
    # Does some error handling.
    response.raise_for_status()

    # access JSON content
    json_response = response.json()

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

# print("Entire JSON response")
# print(json_response)
# # {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.27.1', 'X-Amzn-Trace-Id': 'Root=1-61ec438a-7af1a3ee3c4864f85fc00ddc'}, 'origin': '75.179.180.20', 'url': 'https://httpbin.org/get'}

# for key in json_response.keys():
#     print(f"{key} => {json_response[key]}")
# # args => {}
# # headers => {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.27.1', 'X-Amzn-Trace-Id': 'Root=1-61ec4566-0234036070a801cb0c65fc96'}
# # origin => 75.179.180.20
# # url => https://httpbin.org/get

# We now have a json_response object. Let's try to access some of the values. First, let's get the keys. We could set these to variable if we like.
json_response_keys = json_response.keys()
# print(json_response_keys) # dict_keys(['args', 'headers', 'origin', 'url'])

# Now, get the keys for the 'headers'.
headers_keys = json_response['headers'].keys()
print(headers_keys) # dict_keys(['Accept', 'Accept-Encoding', 'Host', 'User-Agent', 'X-Amzn-Trace-Id'])

# Values for the 'headers'.
headers_values = [json_response['headers'][key] for key in headers_keys]
print(headers_values)   # ['*/*', 'gzip, deflate', 'httpbin.org', 'python-requests/2.27.1', 'Root=1-61ec4bab-5d5029775646cb89411b5828']

# # Zip the 'headers' keys and values.
# # NOTE: This is the same results as using json_response['headers']
# headers_dict = dict(zip(headers_keys,headers_values))
# print(headers_dict) # {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.27.1', 'X-Amzn-Trace-Id': 'Root=1-61ec4c35-53e59d961cbb692050ace8bb'}
# print(json_response['headers'])





#################################################################################
