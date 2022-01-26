# *********************************** #
#              Word Play              #
#   verbing nouns and nouning verbs   #
#             Version: 1.0            #
#         Author: Bruce Stull         #
#              2022-01-23             #
# *********************************** #

# References:
# https://sites.pitt.edu/~naraehan/python3/user_defined_functions.html
    # gerund
# https://www.wikihow.com/Change-a-Verb-to-a-Noun


def verb_a_noun(noun):
    '''Accepts a string 'noun'.
    Returns a string where 'ing' is added to 'noun'.
    '''
    verbed_noun = noun + 'ing'
    return verbed_noun

print(verb_a_noun('facebook'))


# I can't recall, right now, how I used to noun a verb. Will revisit this when I remember.
def noun_a_verb(verb):
    '''Accepts a string 'verb'.
    Returns a string where ??? is done.
    '''
    nouned_verb = ''
    return nouned_verb