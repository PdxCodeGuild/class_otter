# Full Stack Bootcamp - Unit 01 Lab 08
# Justin Hammond, 01/06/2022


'''
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
'''

test_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data_list):
    results = []
    data_length = len(data_list)
    final_index = data_length - 1
    for index in range(data_length):
        if index > 0 and index < final_index:
            left = data_list[index - 1]
            center = data_list[index]
            right = data_list[index + 1]

            if center > left and center > right:
                results.append(index)
        
    return results

def test_peaks():
    assert peaks(test_data) == [6, 14]

def valleys(data_list):
    results = []
    data_length = len(data_list)
    final_index = data_length - 1
    for index in range(data_length):
        if index > 0 and index < final_index:
            left = data_list[index - 1]
            center = data_list[index]
            right = data_list[index + 1]

            if center < left and center < right:
                results.append(index)
        
    return results

def test_valleys():
    assert valleys(test_data) == [9, 17]

def peaks_and_valleys(data_list):
    results = peaks(data_list)
    valley_list = valleys(data_list)

    for valley in valley_list:
        results.append(valley)
    
    results.sort()
    return results

def test_peaks_and_valleys():
    assert peaks_and_valleys(test_data) == [6, 9, 14, 17]

def graph_data(data_list):
    max_value = -1
    for value in data_list:
        if value > max_value:
            max_value = value

    for iteration in range(max_value):
        height = max_value - iteration
        line = ""
        for data in data_list:
            if data >= height:
                line += 'X'
            else:
                line += ' '
        print(line)
    

def main():
    graph_data(test_data)
    print(peaks(test_data))
    print(valleys(test_data))
    print(peaks_and_valleys(test_data))

main()