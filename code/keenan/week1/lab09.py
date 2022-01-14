# Lab 9: Compute Automated Readability Index
# 01/13/2022

# Description:
# Compute the ARI for a given body of text loaded in from a file. The automated readability index 
# (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

# 4.71(characters / words) + 0.5(words/sentences) -21.43

# The score is computed by multiplying the number of characters divided by the number of words by 4.71, adding the number of words divided 
# by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 
# should be presented as having the same age and grade level as scores of 14.

# Scores correspond to the following ages and grad levels:

#     Score  Ages     Grade Level
#      1       5-6    Kindergarten
#      2       6-7    First Grade
#      3       7-8    Second Grade
#      4       8-9    Third Grade
#      5      9-10    Fourth Grade
#      6     10-11    Fifth Grade
#      7     11-12    Sixth Grade
#      8     12-13    Seventh Grade
#      9     13-14    Eighth Grade
#     10     14-15    Ninth Grade
#     11     15-16    Tenth Grade
#     12     16-17    Eleventh grade
#     13     17-18    Twelfth grade
#     14     18-22    College
# Once you’ve computed the ARI score, you can use the ari_scale dictionary below to look up the age range and grade level.


# The output should look something like the following:
# --------------------------------------------------------

# The ARI for gettysburg-address.txt is 12
# This corresponds to a 11th Grade level of difficulty
# that is suitable for an average person 16-17 years old.

# --------------------------------------------------------

# need to import the regular expressions module and the ceil() function from the math module for rounding up
import re
import math


file = input('Provide file to be reviewed: ')
opened_file = open(file, "r", encoding="utf8")
text = opened_file.read()

# this was a Grade 3 level, 65 letters, 4 sentences, 14 words
test_text = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"

# grade 5 from the coleman liau index.  The scoring in this is #3, or grade 2
test_text2 = "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard."

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

# count the number of characters.  Make sure to 
def character_count(text):
    char_list = re.findall(r'[a-zA-Z0-9]', text)
    characters = len(char_list)
    return characters

characters = (character_count(text))


# count the number of sentences by calculating the number of end puncuation marks: (.!?).  split creates an extra '' list item so there is a correction to factor for that
def sentence_count(text):
   sentence_list = re.split("[.?!]", text)
   sentences = len(sentence_list)
   return sentences - 1

sentences = sentence_count(text)


# count the number of words by counting spaces or hyphens, and then adding the number of sentences
def word_count(text):
    word_list = re.split(('[ -]'), text)
    words = len(word_list)
    return words

words = word_count(text)

ari_formula =  4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43

round_up_ari = math.ceil(ari_formula)

# for nested dictionaries in f'strings make sure to use different '' and "" types f
print(f'\nThe ARI for the {file} is {round_up_ari}.\nThis corresponds to a {ari_scale[round_up_ari]["grade_level"]} level of difficulty.\nThat is suitable for an average person of {ari_scale[round_up_ari]["ages"]} years old.')







# can use the Coleman-Liau Index as well: - may not be necessary
# index = 0.0588 * L - 0.296 * S - 15.8

# L is the average number of letters per 100 words in the text
# S is the average number of sentences per 100 words