# Full Stack Bootcamp - Unit 01 Lab 08
# Justin Hammond, 01/06/2022


'''
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

Version 2
Using the data list above, draw the image of X's above.

Version 3
Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the
water is represented by O's. Given data, calculate the amount of water that would be collected.
'''

test_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
test_dat2 = [9, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

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
    assert peaks(test_dat2) == [6, 14]

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
    assert valleys(test_dat2) == [1, 9, 17]

def peaks_and_valleys(data_list):
    results = peaks(data_list)
    valley_list = valleys(data_list)

    for valley in valley_list:
        results.append(valley)
    
    results.sort()
    return results

def test_peaks_and_valleys():
    assert peaks_and_valleys(test_data) == [6, 9, 14, 17]
    assert peaks_and_valleys(test_dat2) == [1, 6, 9, 14, 17]

def get_graph_data(data_list):
    max_value = -1
    for value in data_list:
        if value > max_value:
            max_value = value

    results = ''
    for iteration in range(max_value):
        height = max_value - iteration
        line = ""
        for data in data_list:
            if data >= height:
                line += 'X'
            else:
                line += ' '
        results += f"{line}\n"
    return results

def test_get_graph_data():
    graph_data = ''
    graph_data += '              X     X\n'
    graph_data += '             XXX   XX\n'
    graph_data += '      X     XXXXX XXX\n'
    graph_data += '     XXX   XXXXXXXXXX\n'
    graph_data += '    XXXXX XXXXXXXXXXX\n'
    graph_data += '   XXXXXXXXXXXXXXXXXX\n'
    graph_data += '  XXXXXXXXXXXXXXXXXXX\n'
    graph_data += ' XXXXXXXXXXXXXXXXXXXX\n'
    graph_data += 'XXXXXXXXXXXXXXXXXXXXX\n'    
    assert get_graph_data(test_data) == graph_data

    graph_data = ''
    graph_data += 'X             X     X\n'
    graph_data += 'X            XXX   XX\n'
    graph_data += 'X     X     XXXXX XXX\n'
    graph_data += 'X    XXX   XXXXXXXXXX\n'
    graph_data += 'X   XXXXX XXXXXXXXXXX\n'
    graph_data += 'X  XXXXXXXXXXXXXXXXXX\n'
    graph_data += 'X XXXXXXXXXXXXXXXXXXX\n'
    graph_data += 'XXXXXXXXXXXXXXXXXXXXX\n'
    graph_data += 'XXXXXXXXXXXXXXXXXXXXX\n'    
    assert get_graph_data(test_dat2) == graph_data


def calculate_all_valley_area(data_list):
    peak_list = peaks(data_list)
    valley_list = valleys(data_list)

    if len(valley_list) == 0:
        return 0
    
    should_fill = len(peak_list) == 0 or peak_list[0] > valley_list[0]
    fill_height = data_list[0] if should_fill else 0

    next_peak_index = 0

    filled_heights = []
    for index in range(len(data_list)):
        current_height = data_list[index]
        if should_fill:
            if current_height > fill_height:
                should_fill = False
                fill_height = 0
                filled_heights.append(current_height)
            else:
                filled_heights.append(fill_height)
        else:
            filled_heights.append(current_height)
            if index >= peak_list[next_peak_index]:
                next_peak_index += 1
                should_fill = True
                fill_height = current_height

    return sum(filled_heights) - sum(data_list)

def test_calculate_all_valley_area():
    assert calculate_all_valley_area(test_data) == 18
    assert calculate_all_valley_area(test_dat2) == 58


def main():
    print(get_graph_data(test_data))

    print(peaks(test_data))
    print(valleys(test_data))
    print(peaks_and_valleys(test_data))

    print(calculate_all_valley_area(test_data))

main()