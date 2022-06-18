#2.Python program to extract element with frequency greater than k
l = [1,2,2,2,3,3,3,3,4,4,5,5,5,6,6,7]
k = 2
arr = []
for i in l:
    f = l.count(i)
    if f>k:
        arr.append(i)
print(set(arr))