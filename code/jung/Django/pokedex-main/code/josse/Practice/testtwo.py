import requests
import pprint
while True:

    keyword_search = input("please enter a keyword or done to exit: ")

    page = 1

    if keyword_search == "done":
        print("smell you later")
        break

    while True:
        response = requests.get(
            'http://api.repo.nypl.org/api/v1/items/search.json?', params={"filter": keyword_search,
                                                                          "page": page,
                                                                          },
            headers={'Authorization': 'Token token="6xlhy33h9nxnz934"'})

        qotd = response.json()["nyplAPI"]["request"]

        for quote in qotd:
            print(f"{quote['title']} -- {quote['itemLink']}\n\n")
        next_move = input(
            "would you like to see 'next page' or 'done' to exit: ")
        if next_move == 'next page':
            page += 1
            continue
        elif next_move == 'done':
            break
