'''
*********************************************
*              PDXCode Guild                *
*  Full-Stack Python/JavaScript Day Class   *
*               Class_Otter                 *
*              Scott Madden                 *
*           Lab 14 - Dad Joke API           *
*              24/January/2022              *
*                                           *
*********************************************
'''
#'''
# Part 1
# Import necessary modules
import requests
import json
import time

url = 'https://icanhazdadjoke.com' 
header = {'Accept' : 'application/json'}
parameters = {format:json}
response = requests.get(url, headers=header, params=parameters)
#print(response) # returns HTTP status code. 200 = a successful response return. 
json_res = response.json()
print("\n")
print(json_res['joke'])
print("\n")
print("\n")

#'''mom
#Part 2
while True:
    
    user_input = input("""You can search for Jokes containing specific Search Terms.
Please enter a Search Term for related jokes, or type 'quit' to end:""").lower()

    if user_input == 'quit':
        break
    else:
        url = 'https://icanhazdadjoke.com/search?term={}'.format(user_input) #.format alternate way to ingest the user_input variable.
        # url = f'https://icanhazdadjoke.com/search?term={user_input}' #F-strings allow embed expressions inside string literals.
        headers = {'accept': 'application/json'}
        params = {'limit': 5,}

        response = requests.get(url, headers = headers, params = params)
        data = response.json()
        for i in range(0, len(data['results'])):
            print(data['results'][i]['joke'], end='\n\n')
            time.sleep(4)
#'''            


