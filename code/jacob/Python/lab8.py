'''
Lab 8: Peaks and Valleys
'''
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak = []
valley = []
for i in range(1, (len(data) - 1)):
    if data[i] > data[i+1] and data[i] > data[i-1]:
        peak.append(i)

    elif data[i]< data[i+1] and data[i]< data[i-1]:
        valley.append(i)
print(data)
print(f'Peaks: {peak}')
print(f'Valleys: {valley}')