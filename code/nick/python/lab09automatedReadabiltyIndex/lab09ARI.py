import re

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# ari_score = 4.71 (characters/words) + 0.5 (words/sentences) - 21.43

# with open ('test.txt', 'r') as test_txt:
#    article_lines = test_txt.read()
#    print(article_lines)
   
with open('test.txt', encoding='utf-8') as book:
    article_lines = book.read().lower()

asp = {1: {'age': '5', 'grade': '12'}}


word_count = 0
char_count = 0
for char in article_lines:
    if char == ' ':
        word_count +=1
    else:
        char_count += 1

print(char_count)

punctuation = ['!', '?', '.', ';', ':']

sent_count = 0

for char in article_lines:
    if char in punctuation:
        sent_count += 1
print(sent_count)
print(word_count)
print(char_count)

ari_score = 4.71*(char_count/word_count) + 0.5*(word_count/sent_count) - 21.43
new_score = int(ari_score)
# print(f'The ARI for test.txt score was {new_score}. This corresponds to a {ari_scale[1][]}')
print(f'The ARI score for test.txt is {new_score}.')
print('This corresponds with ages', ari_scale[new_score]['ages'],'at a grade level of', ari_scale[new_score]['grade_level'],'.')