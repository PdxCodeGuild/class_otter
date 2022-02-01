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

    # Make a 'working_list' from 'peaks' so we can work with it.
    working_list = peaks.copy()

    # Add 'valleys' on to the end of 'working_list'. Which is, essentially, adding 'valleys' to 'peaks'.
    working_list.extend(valleys)

    # Sort the 'working_list'.
    working_list.sort()

    # Set 'peaks_and_valleys_list' to 'working_list'.
    peaks_and_valleys_list = working_list
    
    return peaks_and_valleys_list

def test_peaks_and_valleys():
    assert peaks_and_valleys([1,5],[3,6]) == [1,3,5,6]
    assert peaks_and_valleys([1,5,8],[2,3,7]) == [1,2,3,5,7,8]
    assert peaks_and_valleys([6,14], [9,17]) == [6,9,14,17]

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
        # Add just a little space to move the image to line up over the display of 'topography', 'index_list_tens', and 'index_list_ones'.
        result = ' '
        # Loop through the list:
        for i in range(len(topography)):
            # If row value is still above the list value: add ' ' to result string, else: add 'X' to result string.
                if row > topography[i]:
                    result += ' '
                else:
                    result += 'X'
                # Add the two spaces between each column.
                result += '  '
        # Print the result string for current row.
        print(result)

    print(topography, "<== Value Row")

    # Make a list of integers, start at 0 and go until len(topography).
    # Use i // 10 to return the tens digit of the list index. This will keep the 'index' row inline with value row.
    # Use i % 10 to return the ones digit. This will keep the 'index' row inline with value row.
    index_list_ones = []
    index_list_tens = []
    for i in range(len(topography)):
        index_list_tens.append(i // 10)
        index_list_ones.append(i % 10)
    print(index_list_tens, "<== Index Tens")
    print(index_list_ones, "<== Index Ones")

    
main()