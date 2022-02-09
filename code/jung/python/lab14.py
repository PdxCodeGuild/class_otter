import requests
import json


while True:
    term = input("Enter a search term or exit: ")
    if term == "exit":
        break
    else:
        response = requests.get('https://icanhazdadjoke.com/search', params = {"term": term}, headers = {"Accept": "application/json"})

        data = json.loads(response.text)

        quote_data = data["results"] 

        if quote_data == []:
            print("No record found.")
        else:
            for result in quote_data:
                joke = result["joke"]
                print(joke)

