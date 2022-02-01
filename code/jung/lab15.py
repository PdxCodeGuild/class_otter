import requests
import json
#------------------------VERSION 1 -------------------------------#

# def get_random_quote():
#     response = requests.get("https://favqs.com/api/qotd", headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
#     data = json.loads(response.text)
#     data = data["quote"]
#     # pprint.pprint(data)

#     author = data["author"]
#     quote = data["body"]
#     print(f"The author is {author}")
#     print(f'The quote is, "{quote}"')

# get_random_quote()





#------------------------VERSION 2 -------------------------------#

# question = input("enter 'next page' or 'done': ")

def get_random_quote():
    while True:
        page = 1
        filter = input("enter a keyword to search for quotes or exit: ")
        if filter == "exit":
            break


        while True:
            response = requests.get("https://favqs.com/api/quotes?page=<page>&filter=<keyword>", params = {"filter": filter, "page": page}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            data = json.loads(response.text)
            page = data["page"]
            data_of_quote = data["quotes"]


            count = 0
            for quote in data_of_quote:
                if quote["body"] == "No quotes found":
                    count = 0
                elif quote["body"]:
                    count += 1
            print(f"{count} quotes associated with {filter} - page {page}")


            for quote in data_of_quote:
                author = quote["author"]
                quote = quote["body"]
                print(f"{quote} - {author} \n")

    
            ask = input("enter 'next page' or 'done': ")
            if ask == "next page" and data["last_page"] == False:
                page += 1
                continue
            elif ask == "next page" and data["last_page"] == True:
                print("This is the last page.")
                break
            elif ask == "done":
                break

get_random_quote()



