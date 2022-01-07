def is_even(a):
    if a % 2 == 0:
        return True
    return False    

def ones_digit(num):
    x = num % 10
    return x

def tens_digit(num):
    if num < 100:
        x = num // 10
        return x
    elif num > 99 and num < 1000:
        x = ((num % 100) // 10)
        return x

def percentage(v, max):
    x = (100 * float(v / max))
    return round(x, 2)

#print(percentage(35, 70))

def stars(n):
    x = ''
    for num in range(n):
        x += '*'
    return x

#print(stars(5))

def loud_text(text):
    text = text.upper()
    return '-'.join(text)

#print(loud_text('help please'))

def double_letters(word):
    double = ''
    for letter in word:
        double += letter * 2
    return double

#print(double_letters('see'))

def latest_letter(word):
    word = list(word)
    word.sort()
    last = len(word)-1
    return word[last]

#print(latest_letter('apple'))  

def count_hi(text):
    count = text.count('hi')
    return count

#print(count_hi('hi hello hi llama hill'))

def is_empty(d):
    if len(d) == 0:
        return True
    else:
        return False

#print(is_empty({1: 'a', 2: 'b'}))



