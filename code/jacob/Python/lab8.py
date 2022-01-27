'''
Lab 8: Peaks and Valleys
'''
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak = []
valley = []

def peaks(data):
    for i in range(1, (len(data) - 1)):
        if data[i] > data[i+1] and data[i] > data[i-1]:
            peak.append(i)
    return peak
    
def valleys(data):    
    for i in range(1, (len(data) - 1)):    
        if data[i]< data[i+1] and data[i]< data[i-1]:
            valley.append(i)
    return valley

def peaks_and_valleys(a, b):
    return sorted(a + b)

print(data)
print(f'Peaks: {peaks(data)}')
print(f'Valleys: {valleys(data)}')

print(f'Peaks and Valleys: {peaks_and_valleys(peak, valley)}')