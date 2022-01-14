data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks():
    current = [i for i in data]
    previous = [i - 1 for i in data if data[i] >= 0]
    next = [i + 1 for i in data if data[i] >= 0]
    
    
    
    # print(previous)
    # print(next)
    # s = [print(i) for i in data if current[i]>previous[i]]

# def peaks_and_valleys():
set1 = peaks()
print(set1)