import requests

response = requests.get('https://api.ipify.org')
print(response.url)
print(response.text) # 76.105.187.182
print(response.status_code) # 200
print(response.encoding) # ISO-8859-1
print(response.headers) # {'Content-Type': 'text/plain', 'Content-Length': '14', ...}