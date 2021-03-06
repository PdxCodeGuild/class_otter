import requests
import time
from random import choice

term = input("Give me a topic that your dad loves to joke about: ")

response_json = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": term}
).json()

results = response_json["results"]

total_jokes = response_json["total_jokes"]

countdown = ['3', '2', '1']

if total_jokes == 1:
    print(
        f"\nYou're in luck, I have only one joke about {term}. Wait for it........."
    )
    countdown = [(time.sleep(1), print(count)) for count in countdown] #simplified the countdown
    # first attempt at countdown
    # time.sleep(1)
    # print("1\n")
    # time.sleep(1)
    # print("2\n")
    # time.sleep(1)
    # print("3\n")
    # time.sleep(1)
    print(results[0]['joke'])
    
elif total_jokes > 1:
    print(
        f"I have found {total_jokes} jokes relating to {term}.  Here's a random one:\n",
        choice(results)['joke']
    )
else:
    print(f"Wow, your dad was a weirdo, I don't have a single joke about {term}!\nHere's a random joke about something else instead:\n")
    random_json = requests.get(
        "https://icanhazdadjoke.com/",
        headers={"Accept": "application/json"}
    ).json()
    random = random_json['joke']
    print(random)