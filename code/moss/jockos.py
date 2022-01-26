
jacklopes = [0,0]

year = 0

while len(jacklopes) < 1000 :
         
    for i in range(len(jacklopes)):

        if jacklopes[i] >= 4 and jacklopes[i] <=8: # this will give different numbers depending on what age they start at when born.
            jacklopes.append(0)    
    
    for i in range(len(jacklopes)-1, -1, -1):
        if jacklopes[i] == 10:
            jacklopes.remove(jacklopes[i])
    

    for i in range(len(jacklopes)):
        if jacklopes[i] < 10 :
            jacklopes[i]+=1

    year+= 1

print(len(jacklopes))

print(year)