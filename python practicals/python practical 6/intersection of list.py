def inter(a,b):
    c = [i for i in a if i in b]
    return c 
a = [1,3,2,4,5,6,7,8]
b = [3,4,5,6,7,8,9,10]
print(inter(a,b))