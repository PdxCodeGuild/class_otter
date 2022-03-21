# Full Stack Bootcamp - Unit 01 Lab 15
# Justin Hammond, 01/12/2022

'''
Lab 15: Quotes API
For this lab we'll be using the Favqs Quotes API to first get a random
quote, and then allow the user to find quotes by keyword. To accomplish
this we'll be using the requests library.


Version 1: Get a Random Quote
The URL to get a random quote is https://favqs.com/api/qotd, send a
request here, parse the JSON in the response into a python dictionary,
and show the quote and the author.


Version 2: List Quotes by Keyword
The Favqs Quote API also supports getting a list of quotes associated
with a given keyword
https://favqs.com/api/quotes?page=<page>&filter=<keyword>. Prompt the
user for a keyword, list the quotes you get in response, and prompt the
user to either show the next page or enter a new keyword. You can use
string concatenation to build the URL.

> enter a keyword to search for quotes: nature
25 quotes associated with nature - page 1
<list of quotes>
> enter 'next page' or 'done': next page
25 quotes associated with nature - page 2
<list of quotes>
> enter 'next page' or 'done': done
> enter a keyword to search for quotes:

This API endpoint requires an API key be included in a request header.
You can find documentation of specifying request headers here and
documentation on authorization with the Favqs API here under
"Authorization".

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
Other Quote APIs
    Programming Quotes
    Quotes Garden
        get random quote https://quote-garden.herokuapp.com/quotes/random
        get quotes by keyword https://quote-garden.herokuapp.com/quotes/search/<keyword/
'''
import requests


def request_quote():
    response = requests.get('https://favqs.com/api/qotd', headers={'Content-Type': 'application/json'}).json()
    return response['quote']['body'], response['quote']['author']

def get_quote_string(quote, author):
    return f'{quote}\n\t- {author}'

def search_quote(search_term, page=1):
    response = requests.get('https://favqs.com/api/quotes',
                            params={
                                'filter': search_term,
                                'page': page},
                            headers={
                                'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                                'Content-Type': 'application/json'}
                                ).json()
    return SearchResults(response, search_term)


class SearchResults:
    def __init__(self, response, search_term):
        self._results = []
        for item in response['quotes']:
            self._results.append([item['body'], item['author']])
        self._search_term = search_term
        self._current_index = 0
        self._current_page = response['page']
        self._is_last_page = response['last_page']

    def next(self):
        if self._current_index < len(self._results):
            quote, author = self._results[self._current_index]
            self._current_index += 1
            return quote, author, self
        else:
            if self._is_last_page:
                return None, None, None
            else:
                self = search_quote(self._search_term, self._current_page + 1)
                return self.next()

    def get_quote_count(self):
        count = len(self._results)
        if self._is_last_page:
            return count
        else:
            if count >= 25:
                return '25+'
            else:
                return count


def main():
    while True:
        search_term = input("Search for a quote or [Q]uit: ")
        if search_term.upper() == 'Q':
            break
        search_results = search_quote(search_term)
        print(f'Found {search_results.get_quote_count()} quotes about "{search_term}"\n')
        while True:
            quote, author, search_results = search_results.next()
            if quote == None:
                print("\nSorry, no more quotes\n")
                break
            print(get_quote_string(quote, author))
            should_continue = input("Get [N]ext quote or [D]one? ").upper() == 'N'
            print(' ')
            if not should_continue:
                break
    
main()