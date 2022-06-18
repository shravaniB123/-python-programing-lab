#5.Write a python program to compute difference between two list
from collections import Counter
l1 = [1,2,3,4,5,6]
l2 = [3,4,5,6,7,8]
#arr = []
#for i in range(len(l1)):
#   if i in l1:
#       if i not in l2:
#           arr.append(i)
#print(arr)
A = Counter(l1)
B = Counter(l2)
print(list(A-B))
print(list(B-A))