data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(enterdata):
    peakslist = []
    for x in range(1, len(enterdata) - 1):
        if enterdata[x + 1] < enterdata[x] > enterdata[x - 1]:
            # peakslist.append(enterdata[x])
            peakslist.append(x)
    print(f"peaks(data):\n{peakslist}")
def valleys(enterdata):
    valleylist = []
    valleylistv = []
    # print(len(enterdata))
    for x in range(1, len(enterdata) - 1):
        if enterdata[x + 1] > enterdata[x] <enterdata[x - 1]:
            valleylistv.append(enterdata[x])
            valleylist.append(x)
    print(f"valleys(data):\n{valleylist}")
def peaks_and_valleys(enterdata):
    peaksvalleylist = []  
    for x in range(1, len(enterdata) - 1):
        if enterdata[x + 1] > enterdata[x] <enterdata[x - 1] or enterdata[x + 1] < enterdata[x] > enterdata[x - 1]:
            # peaksvalleylist.append(enterdata[x])
            peaksvalleylist.append(x)
    print(f"peask_and_valleys:\n{peaksvalleylist}")

peaks(data)
valleys(data)
peaks_and_valleys(data)