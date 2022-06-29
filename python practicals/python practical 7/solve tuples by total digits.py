#5. Python program to solve tuples by total digits
def count(t):
    return sum([len(str(ele)) for ele in t])
list = [(3,4,6,723),(1,2),(12345,),(134,234,34)]
print("The original list is: "+str(list))
list.sort(key = count)
print("Sorted tuple is: "+str(list))