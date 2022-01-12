from typing import final


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]



def peaks(data):
    info1 = []
    for i in range(len(data)):
        if i != len(data) - 1:
            if data[i] > data[i - 1] and data[i] > data[i + 1]:
                info1.append(i)
    return info1

print(f"Peaks are: {peaks(data)}")

def valleys(data):
    info2 = []
    for i in range(len(data)):
        if i != len(data) - 1 and i != 0:
            if data[i] < data[i - 1] and data[i] < data[i + 1]:
                info2.append(i)
    return info2

print(f"Valleys are: {valleys(data)}")



def peaks_and_valleys():
    final_list = peaks(data) + valleys(data)
    final_list.sort()
    return final_list

print(f"Peaks and Valleys are: {peaks_and_valleys()}")


# number = 0
# for x in data:
#     if x >= number:
#         number = x
# # print(number)


# for x in range(number, 0, -1):
#     # print(x) = 9 8 7 6 5 4 3 2 1
#     print_string = ""
#     for num in data:
#         # print(num)
#         if num >= x:
#             print_string += " X "
#         else:
#             for i in range(len(data)):
#                 if data[i] > data[i + 1]:
#                     print_string += " O "
#                 else:
#                     print_string += "   "
#     print(print_string)


