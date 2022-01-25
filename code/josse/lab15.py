import requests
import pprint
while True:

    keyword_search = input("please enter a keyword or done to exit: ")
    # page_search = input("please enter a page: ")

    page = 1

    if keyword_search == "done":
        print("smell you later")
        break

    while True:
        response = requests.get(
            'https://favqs.com/api/quotes?', params={"filter": keyword_search,
                                                     "page": page,
                                                     },
            headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

        qotd = response.json()["quotes"]

        for quote in qotd:
            print(f"{quote['author']} -- {quote['body']}\n\n")
        next_move = input(
            "would you like to see 'next page' or 'done' to exit: ")
        if next_move == 'next page':
            page += 1
            continue
        elif next_move == 'done':
            break
