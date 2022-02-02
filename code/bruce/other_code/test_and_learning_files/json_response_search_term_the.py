the_json_response = {'current_page': 1, 'limit': 20, 'next_page': 2, 'previous_page': 1, 'results': [{'id': '69xAsrHYDAd', 'joke': 'Why did Mozart kill all his chickens?\r\nBecause when he asked them who the best composer was, they\'d all say "Bach bach bach!"\r\n'}, {'id': 'aMmbaFYTKBd', 'joke': "I finally bought the limited edition Thesaurus that I've always wanted. When I opened it, all the pages were blank.\r\nI have no words to describe how angry I am."}, {'id': 'lbU01DljGtc', 'joke': "I couldn't get a reservation at the library. They were completely booked."}, {'id': 'caxscaMRnjb', 'joke': "Did you know the first French fries weren't actually cooked in France? They were cooked in Greece."}, {'id': 'ci311DtH6h', 'joke': 'I’ll tell you something about German sausages, they’re the wurst'}, {'id': 'lyk3EIBQfxc', 'joke': 'I went to the zoo the other day, there was only one dog in it. It was a shitzu.'}, {'id': 'm3wPZoz51ob', 'joke': 'Did you hear the news? FedEx and UPS are merging. They’re going to go by the name Fed-Up from now on.'}, {'id': '82wHlbaapzd', 'joke': "Me: If humans lose the ability to hear high frequency volumes as they get older, can my 4 week old son hear a dog whistle?\r\n\r\nDoctor: No, humans can never hear that high of a frequency no matter what age they are.\r\n\r\nMe: Trick question... dogs can't whistle."}, {'id': 'mbpbapbhiyd', 'joke': 'Did you hear about the bread factory burning down? They say the business is toast.'}, {'id': '8hFYojqz5h', 'joke': "Why don't skeletons ride roller coasters? They don't have the stomach for it."}, {'id': 'nWvcUD5orrc', 'joke': 'I asked the surgeon if I could administer my own anesthetic, they said: go ahead, knock yourself out.'}, {'id': '9hiGeNZ0Tnb', 'joke': 'They tried to make a diamond shaped like a duck. It quacked under the pressure.'}, {'id': 'exXSCtkOKe', 'joke': 'Why do pirates not know the alphabet? They always get stuck at "C".'}, {'id': 'f211DdFBdxc', 'joke': "Did you hear about the chameleon who couldn't change color? They had a reptile dysfunction."}, {'id': '2giGYLeiGe', 'joke': 'Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.'}, {'id': 'obahq4MJtzd', 'joke': 'I had a rough day, and then somebody went and ripped the front and back pages from my dictionary. It just goes from bad to worse.'}, {'id': 'A5MCY821gib', 'joke': "Why do bees hum? Because they don't know the words."}, {'id': 'AAIYo4MJmrc', 'joke': 'A magician was driving down the street and then he turned into a driveway.'}, {'id': 'AXnrrcNmyAd', 'joke': 'Why do bananas have to put on sunscreen before they go to the beach? Because they might peel!'}, {'id': 'pjyA59MRusc', 'joke': 'There’s a new type of broom out, it’s sweeping the nation.'}], 'search_term': 'the', 'status': 200, 'total_jokes': 390, 'total_pages': 20}

keys_object = the_json_response.keys()

the_keys = []
for key in keys_object:
    the_keys.append(key)

print(the_keys)
['current_page', 'limit', 'next_page', 'previous_page', 'results', 'search_term', 'status', 'total_jokes', 'total_pages']

# Pop the key 'results' from the list and see what remains. 'results' is the key which holds the jokes.
the_keys.pop(the_keys.index('results'))

joke_keys_object = the_json_response['results'].keys()
print(joke_keys_object)

print(the_keys)
['current_page', 'limit', 'next_page', 'previous_page', 'search_term', 'status', 'total_jokes', 'total_pages']

for key in the_keys:
    print(f"{key} : {the_json_response[key]}")
# current_page : 1
# limit : 20
# next_page : 2
# previous_page : 1
# search_term : the
# status : 200
# total_jokes : 390
# total_pages : 20

# Get the jokes from the json.
# NOTE: The 'results' key holds a list of 'joke' dictionaries.
the_jokes = the_json_response.pop('results')

# How many jokes do we have? It seems the default return number of jokes is 20.
print(type(the_jokes), len(the_jokes))
# <class 'list'> 20