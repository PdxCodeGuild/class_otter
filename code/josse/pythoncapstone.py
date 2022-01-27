import requests
# import pprint
# NYPL Token - 6xlhy33h9nxnz934
response = requests.get('http://api.repo.nypl.org/api/v1/items/search?q=[search-terms]&publicDomainOnly=true',
                        headers={'Authorization': 'Token token="6xlhy33h9nxnz934"'})

books = response.json()
# pprint.pprint(books)
print(books)
# print(jokes)
