'''
*********************************************
*              PDXCode Guild                *
*  Full-Stack Python/JavaScript Day Class   *
*               Class_Otter                 *
*              Scott Madden                 *
*           Lab 15 - Quotes API             *
*              26/January/2022              *
*                                           *
*********************************************
'''
#Version 1 Complete
import requests

"""
url = 'https://favqs.com/api/qotd'
response = requests.get(url)
print(response)
data = response.json()
# print(data['quote']['body'], data['quote']['author'])
random_quote = data['quote']['body']
author = data['quote']['author']
print(random_quote, author)
"""

#Version 2 Complete

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
welcome = input('Welcome to the Quotes, would you like to continue? (yes/no): ')
parameters = {'page' : 1}
# page = 1
url = (f"https://favqs.com/api/quotes?page={parameters['page']}&filter=")
# print(url)
while welcome == 'yes':
    keyword = input('Please enter a keyword: ')
    final_url = url + keyword

    response = requests.get(final_url, headers=headers)
    # print(response)
    data = response.json()
    # print(data)
    num = 0

    for i in data['quotes']:
        print(f"{data['quotes'][num]['body']}")
        print('')
        parameters['page'] = 1
        num += 1
        if num == 25:
            question = input('Would you like to view the next page? (yes/no): ')
            while question == 'yes':
                num = 0
                parameters['page'] += 1
                final_url = (f"https://favqs.com/api/quotes?page={parameters['page']}&filter={keyword}")
                response = requests.get(final_url, headers=headers)
                data = response.json()
                for j in data['quotes']:
                    print(f"{data['quotes'][num]['body']}")
                    print('')
                    num += 1
                
                question = input('Next page?: ')
            else:
                break


    welcome = input('Would you like to see more Quotes?(yes/no): ')

print('Good Bye!')

