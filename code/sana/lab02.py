nlist = []
def sum(nlist):
    main = 0
    for position in range(len(nlist)):
        main = main + nlist[position]
    return main

alist = []
user = input("Enter a number to be added to the list, once finished type 'done': ")
user = user.lower()
while user != "done":
    user = int(user)
    alist.append(user)
    user = input("Enter a number to be added to the list, once finished type 'done': ")
result = sum(alist)
print(f"Numbers: {alist}")
print(f"Average: {result}")

elist = [5, 0, 8, 3, 4, 1, 6]
sum(elist)
e_total = sum(elist)
e_average = e_total / len(elist)
print()
print(e_total)
print()
print(e_average)
average = result / len(alist)
print()
print(average)
print()