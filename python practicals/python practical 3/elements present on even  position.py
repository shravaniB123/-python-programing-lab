#2.Python program to print elements of array present on even position
arr = [12,23,43,25,65,11]
print("The array is:",arr)
print("The elements in even positions:")
for i in range(0,len(arr),2):
    print(arr[i])