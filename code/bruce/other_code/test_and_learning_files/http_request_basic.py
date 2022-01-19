# *************************** #
#        HTTP Requests        #
#   Uses 'requests' library   #
#         Version: 0.0        #
#     Author: Bruce Stull     #
#          2022-01-17         #
# *************************** #

# Resources:
# https://github.com/brucestull/PDX_Full_Stack/blob/bruce/1%20Python/docs/15%20Requests.md

# Needed to install requests
# In terminal:
    # pip install requests

import requests
import json

############# Request without params ################
# response = requests.get('https://api.ipify.org')

# print(f"type(response): {type(response)}")
# print(f"response.url: {response.url}")
# print(f"response.text: {response.text}") # 76.105.187.182
# print(f"response.status_code: {response.status_code}") # 200
# print(f"respong.encoding: {response.encoding}") # ISO-8859-1
# print(f"response.headers: {response.headers}")

# type(response): <class 'requests.models.Response'>
# response.url: https://api.ipify.org/
# response.text: 75.179.180.20
# response.status_code: 200
# respong.encoding: ISO-8859-1
# response.headers: {'Server': 'Cowboy', 'Connection': 'keep-alive', 'Content-Type': 'text/plain', 'Vary': 'Origin', 'Date': 'Mon, 17 Jan 2022 22:22:47 GMT', 'Content-Length': '13', 'Via': '1.1 vegur'}
#####################################################


# ########### Request with params ###########
# response = requests.get('https://api.ipify.org', params={'format': 'json'})

# print(f"type(response): {type(response)}")
# print(f"response.url: {response.url}")
# print(f"response.text: {response.text}") # 76.105.187.182
# print(f"response.status_code: {response.status_code}") # 200
# print(f"respong.encoding: {response.encoding}") # ISO-8859-1
# print(f"response.headers: {response.headers}")

# # type(response): <class 'requests.models.Response'>
# # response.url: https://api.ipify.org/?format=json
# # response.text: {"ip":"75.179.180.20"}
# # response.status_code: 200
# # respong.encoding: utf-8
# # response.headers: {'Server': 'Cowboy', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Vary': 'Origin', 'Date': 'Mon, 17 Jan 2022 22:24:52 GMT', 'Content-Length': '22', 'Via': '1.1 vegur'}
# ###########################################

# If the response is in JSON, you can turn it into a python dictionary using the json.loads() function
# or the json() method on the response object. You can then extract the relevant data.

################### Using json.loads() funcion or json() method #################
response = requests.get('https://api.ipify.org', params={'format': 'json'})

print(response.text) # {"ip":"76.105.187.182"} - raw json response
data = response.json() # turn raw json into a python dictionary
print(data) # {'ip': '76.105.187.182'} - python dictionary
print(data['ip']) # 76.105.187.182

# {"ip":"75.179.180.20"}
# {'ip': '75.179.180.20'}
# 75.179.180.20

data = json.loads(response.text) # use the json library to parse the raw response
print(data) # {'ip': '76.105.187.182'} - python dictionary
print(data['ip']) # 76.105.187.182

# {'ip': '75.179.180.20'}
# 75.179.180.20

print(response.headers['Date'])
#################################################################################
