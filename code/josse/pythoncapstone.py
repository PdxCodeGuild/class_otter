import requests
import pprint

user = input("what would you like to search: ")

url = 'http://api.repo.nypl.org/api/v1/items/search.json?q=' + user
auth = 'Token token=6xlhy33h9nxnz934'
call = requests.get(url, headers={'Authorization': auth})


# # NYPL Token - 6xlhy33h9nxnz934
# response = requests.get(
#     'http://jperez:wanted12@api.repo.nypl.org/api/v1/items/search?q=[search-terms]&publicDomainOnly=true')
# headers={'Authorization': 'Token token="6xlhy33h9nxnz934"'})

books = call.json()
pprint.pprint(books)
# print(books)
