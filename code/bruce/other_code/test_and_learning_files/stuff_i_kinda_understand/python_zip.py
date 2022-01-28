# *************************************************** #
#             Using zip() tuple() range()             #
#   Needed to generate the tuple for cross diagonal   #
#                     Version: 0.0                    #
#                 Author: Bruce Stull                 #
#                      2022-01-22                     #
# *************************************************** #

zipped_thingamabob = list(zip(range(3),range(2,-1,-1)))
print(zipped_thingamabob)   # [(0, 2), (1, 1), (2, 0)]

zipped_thingamabob = tuple(zip(range(3),range(2,-1,-1)))
print(zipped_thingamabob)   # ((0, 2), (1, 1), (2, 0))