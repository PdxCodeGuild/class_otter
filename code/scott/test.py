def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
         
# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))