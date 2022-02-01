
jackalope_list = [0, 0]

def jackalope_married(jackalope_list):
    for jackalope in range(len(jackalope_list)):
        if jackalope_list[jackalope] >= 4 and jackalope_list[jackalope] <= 8:
                jackalope_list.append(0)
def jackalope_expired(jackalope_list):
    while 10 in jackalope_list:
        jackalope_list.remove(10)
def jackalope_aged(jackalope_list):
    for year in range(len(jackalope_list)):
        jackalope_list[year] += 1
# print(jackalope_list)
# jackalope_expired()
# print(jackalope_list)
# jackalope_married()
# print(jackalope_list)
# jackalope_aged()
# print(jackalope_list)
# print(len(jackalope_list))

year = 0
while len(jackalope_list) <= 1000:
    # print(jackalope_list)
    jackalope_expired(jackalope_list)
    # print(jackalope_list)
    jackalope_married(jackalope_list)
    # print(jackalope_list)
    jackalope_aged(jackalope_list)
    # print(jackalope_list)
    # print(len(jackalope_list))
    year += 1
    print(year)