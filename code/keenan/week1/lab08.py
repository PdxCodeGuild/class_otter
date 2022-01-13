# Lab 8: Peaks and Valleys

# Define the following functions:

# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak_list = []
valleys_list = []
both_list = []


def peaks(data):
    for i in range(1, len(data) -1):
        if data[i - 1] < data[i] and data[i] > data[i + 1]:
            peak = i
            peak_list.append(peak)
            i += 1
        else:
            i += 1
    print(peak_list)

    
# list comphrehension format: [output] [for var in a_list] [(optional condition)]
    #  peaks = n for n in data if     
peaks(data)    


def valleys(data):
    for i in range(1, len(data) -1):
        if data[i - 1] > data[i] and data[i] < data[i + 1]:
            valley = i
            valleys_list.append(valley)
            i += 1
        else:
            i += 1
    print(valleys_list)
 

valleys(data)


def peak_and_valleys(data):
    for i in range(1, len(data) -1):
        if (data[i - 1] > data[i] and data[i] < data[i + 1]) or (data[i - 1] < data[i] and data[i] > data[i + 1]):
            index = i
            both_list.append(index)
            i += 1
        else:
            i += 1
    print(both_list)

peak_and_valleys(data)