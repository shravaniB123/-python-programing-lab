#4.Python program to copy all elements of one array into another
arr1 = [2,5,43,6,7,3,5]
arr2 = [None]*len(arr1)
for i in range(0,len(arr1)):
    arr2[i] = arr1[i]
print("Elements of original array:")
for i in range(0,len(arr1)):
    print(arr1[i])

print("Elements of new array:")
for i in range(0,len(arr2)):
    print(arr2[i])