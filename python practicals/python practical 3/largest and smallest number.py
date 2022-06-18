#3.Python program to print largest and smallest elements in array
arr = [10,89,9,56,4,80,8]
min = arr[0]
max = arr[0]
print("Min and max elements are:")
for i in range(len(arr)):
    if arr[i]<min:
        min = arr[i]
    if arr[i]>max:
        max = arr[i]
print(min)
print(max)