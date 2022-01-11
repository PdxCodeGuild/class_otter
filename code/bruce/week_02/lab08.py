# **************************** #
#   Lab 8: Peaks and Valleys   #
#     Functions, Max, Min      #
#         Version: 2.0         #
#     Author: Bruce Stull      #
#          2022-01-11          #
# **************************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/1%20Python/labs/08%20Peaks%20And%20Valleys.md

# Define the following functions:
# 1. `peaks` - Returns the indices of peaks. A peak has a lower number on both the left and the right.
# 2. `valleys` - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
# 3. `peaks_and_valleys` - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
            
topography = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(list = []):
    '''Accepts a list of integers. Returns a list of indexes of values which are (peaks).'''
    peaks_list = []
    # Index starts at '1' since the first element can't be a peak.
    # Index end at len(list) - 1 since last element can't be a peak.
    
    # Using list comprehension:
    peaks_list = [i for i in range(1, len(list) - 1) if (list[i -1] < list[i] and list[i] > list[i + 1])]

    return peaks_list

def test_peaks():
    assert peaks() == []
    assert peaks([1,1,1]) == []
    assert peaks([1,2,1]) == [1]
    assert peaks([1,2,3,2,3,2,1]) == [2,4]
    assert peaks([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]) == [6,14]

def valleys(list = []):
    '''Accepts a list of integers. Returns a list of indexes of values which are (valleys)'''
    valleys_list = []
    # Index starts at '1' since the first element can't be a valley.
    # Index end at len(list) - 1 since last element can't be a valley.
    # Using for loop:
    for i in range(1, len(list) - 1):
        if list[i - 1] > list[i] and list[i] < list[i + 1]:
            valleys_list.append(i)
    return valleys_list

def test_valleys():
    assert valleys() == []
    assert valleys([1,1,1]) == []
    assert valleys([2,1,2]) == [1]
    assert valleys([1,2,3,2,3,2,1]) == [3]
    assert valleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]) == [9,17]

def peaks_and_valleys(peaks = [], valleys = []):
    '''This function is really just a list combiner and sorter.'''
    # We could try to 'zipper' them together in order, since they are already in order.
    # We could extend() one onto the other then sort() them.
    # Or we could 'filter' the elements through each of the peaks() and valleys() functions
    # as we go through them. This doesn't really make sense, though. Don't think it could work that way.
    peaks.extend(valleys)
    # Create a new list from POIs in peaks (peaks currently includes both peaks and valleys).
    peaks_and_valleys_list = peaks.copy()
    peaks_and_valleys_list.sort()
    return peaks_and_valleys_list

def test_peaks_and_valleys():
    assert peaks_and_valleys([1,5],[3,6]) == [1,3,5,6]
    assert peaks_and_valleys([1,5,8],[2,3,7]) == [1,2,3,5,7,8]
    assert peaks_and_valleys(peaks(topography), valleys(topography)) == [6,9,14,17]

def main():
    print(f'''
    Peaks: {peaks(topography)}
    Valleys: {valleys(topography)}
    Peaks and Valleys: {peaks_and_valleys(peaks(topography), valleys(topography))}
    ''')

    # I want to print 'X's the same number of times of the value of each element in the list.

    # Two spaces are added between columns.

    # Starting from the top down, it seems like we print empty space,
    # and then start filling in the peaks.

    # It seems we need to use the max() value of peaks() to start the print process.

    

    #                   X   
    #                X  X  X
    #             X  X  X  X  X
    small_list = [1, 2, 3, 2, 1]
    
    
    # Loop through rows:
    for row in range(max(topography), 0, -1):
        result = ' '
        # Loop through the list:
        for i in range(len(topography)):
            # If row value is still above the list value: print space, else: print 'X'.
                if row > topography[i]:
                    result += ' '
                else:
                    result += 'X'
                result += '  '
        print(result)

    print(topography)
    # First row = 0 :
    result  = ""
    result += " "
    result += "  "
    result += " "
    result += "  "
    result += "X"

    # Second row = 1 :
    result  = ""
    result += " "
    result += "  "
    result += "X"
    result += "  "
    result += "X"
    result += "  "
    result += "X"

    # Third row = 2 :
    result  = ""
    result += "X"
    result += "  "
    result += "X"
    result += "  "
    result += "X"
    result += "  "
    result += "X"
    result += "  "
    result += "X"



    row_01  = "      X"
    row_02  = "   X  X  X"
    row_03  = "X  X  X  X  X"
    sm_list = [1, 2, 3, 2, 1]
    # print(max(sm_list))

    # if row number > list[i]: print space, add two spaces, if row number > list[i + 1]: print space, ...
    #          X            X            X            X
    row_i   = " " + "  " + " " + "  " + " " + "  " + " "
    
main()