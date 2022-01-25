import requests
import json
import time



term = input("Enter a search term: ")

# # printing the start time
# print("The time of code execution begin is : ", end="")
# print(time.ctime())

# # using sleep() to hault the code execution
# time.sleep(6)

# # printing the end time
# print("The time of code execution end is : ", end="")
# print(time.ctime())

response = requests.get('https://icanhazdadjoke.com/search', params = {"term": term}, headers = {"Accept": "application/json"})

# print(response.text)

data = json.loads(response.text)
print(data)


for result in data["results"]:
    print(result["joke"])