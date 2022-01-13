# Lab09.py Compute Automated Readability Index - 22-01-12

 
#import re


# def search_text():
with open('Gettysburg_Address.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    number_of_characters = len(contents)
    number_of_words = contents.split()
    number_of_sentences = len(contents.split('[\n]'))
    
    # lines = 0
    # blanklines = 0
    # for line in contents:
    #     print line,
    #     lines += 1
    # if line.startswith('\n'):
    #     blanklines += 1
    # else:
    #     sentences += line.count('.') + line.count('!') + line.count('?')
    print('\nNumber of characters in text file :', number_of_characters)    
    print('\nNumber of words in text file :', len(number_of_words))
    print('\nNumber of number_of_sentences in text file:', number_of_sentences)

# (re.split('[.?!]', contents)) 
    # number_of_number_of_lines = contents.readnumber_of_lines()
    # print('Number of number_of_lines in tex file:', number_of_number_of_lines)       
    # contents = f.read()
    # number_of_lines = 0
    # for line in contents:
    #     if line = "\n":
    #         number_of_lines += 1

        




# ari_scale = {
#      1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
#      2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
#      3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
#      4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
#      5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
#      6: {'ages': '10-11', 'grade_level':    '5th Grade'},
#      7: {'ages': '11-12', 'grade_level':    '6th Grade'},
#      8: {'ages': '12-13', 'grade_level':    '7th Grade'},
#      9: {'ages': '13-14', 'grade_level':    '8th Grade'},
#     10: {'ages': '14-15', 'grade_level':    '9th Grade'},
#     11: {'ages': '15-16', 'grade_level':   '10th Grade'},
#     12: {'ages': '16-17', 'grade_level':   '11th Grade'},
#     13: {'ages': '17-18', 'grade_level':   '12th Grade'},
#     14: {'ages': '18-22', 'grade_level':      'College'}
# }

