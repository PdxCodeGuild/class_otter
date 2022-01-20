data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peak = []
    for i in range(1, len(data)-1):
        if data[i]>data[i + 1] and data[i - 1]< data[i]:
            peak.append(i)
    return(peak)


print(peaks(data))

def valley(data):
    valley = []
    for i in range(1, len(data)-1):
        if data[i]<data[i + 1] and data[i - 1]> data[i]:
            valley.append(i)
    return(valley)
print(valley(data))

def peak_and_valley(data):
    peak_and_valley = []
    for i in range(1, len(data)-1):
        if data[i]<data[i + 1] and data[i - 1]> data[i]:
            peak_and_valley.append(i)
    
    for i in range(1, len(data)-1):
        if data[i]>data[i + 1] and data[i - 1]< data[i]:
            peak_and_valley.append(i)
    return(peak_and_valley)

print(peak_and_valley(data))