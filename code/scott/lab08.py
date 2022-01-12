# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# Index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def peaks(elevation):
    peaks = []
    for i in range(1,len(elevation)-1):
        left_num = elevation[i - 1]
        middle_num = elevation[i]
        right_num = elevation[i + 1]
        if left_num < middle_num > right_num:
            peaks.append(i)
    return peaks

def valleys(elevation):
    valleys = []
    for i in range(1,len(elevation)-1):
        left = elevation[i - 1]
        middle = elevation[i]
        right = elevation[i + 1]
        if left > middle < right:
            valleys.append(i)
    return valleys
def p_v_s(elevation):
    highs = peaks(elevation)
    lows = valleys(elevation)
    return sorted(highs + lows)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(data)
    print('peaks', peaks(data))
    print('valleys', valleys(data))
    print('peaks_and_valleys', p_v_s(data))
    print()