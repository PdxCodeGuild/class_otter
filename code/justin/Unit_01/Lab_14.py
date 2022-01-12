# Full Stack Bootcamp - Unit 01 Lab 14
# Justin Hammond, 01/11/2022

'''
Lab 14: Dad Joke API
Use the Dad Joke API to get a dad joke and display it to the user. You
may want to also use time.sleep to add suspense.

Part 1
Use the requests library to send an HTTP request to
https://icanhazdadjoke.com/ with the accept header as application/json.
This will return a dad joke in JSON format. You can then use the .json()
method on the response to get a dictionary. Get the joke out of the
dictionary and show it to the user.

Part 2 (optional)
Add the ability to "search" for jokes using another endpoint. Create a
REPL that allows one to enter a search term and go through jokes one at
a time. You can also add support for multiple pages.
'''
import requests


def request_joke():
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'}).json()
    return response['joke']

def search_joke(search_term, page=1):
    response = requests.get('https://icanhazdadjoke.com/search', params={'term': search_term}, headers={'Accept': 'application/json'}).json()
    return SearchResults(response)


class SearchResults:
    def __init__(self, response):
        self._results = []
        for item in response['results']:
            self._results.append(item['joke'])
        self._current_joke_index = 0
        self._search_term = response['search_term']
        self._joke_count = response['total_jokes']
        self._current_page = response['current_page']
        self._page_count = response['total_pages']

    def next(self):
        if self._current_joke_index < len(self._results):
            joke = self._results[self._current_joke_index]
            self._current_joke_index += 1
            return joke
        else:
            if self._current_page < self._page_count:
                self = SearchResults(search_joke(self._search_term, self._current_page + 1))
                return self.next()
            else:
                next_joke = None
        return next_joke

    def get_joke_count(self):
        return self._joke_count



def main():
    while True:
        search_term = input("Search for a joke or [Q]uit: ")
        if search_term.upper() == 'Q':
            break
        search_results = search_joke(search_term)
        print(f'Found {search_results.get_joke_count()} total jokes about "{search_term}"\n')
        while True:
            dad_joke = search_results.next()
            if dad_joke == None:
                print("\nSorry, no more jokes\n")
                break
            print(dad_joke)
            should_continue = input("Get another joke? [Y]es or [N]o: ").upper() == 'Y'
            print(' ')
            if not should_continue:
                break


main()