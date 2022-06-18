#6.Write a python program to print all pronic numbers between 1 and 100
#Pronic number is the product of consecutive integer
import math
print("Pronic numbers between 1 and 100 are:")
for i in range(1,101):
    for j in range(int(math.sqrt(i))+1):
        if j*(j+1)==i:
            print(i)
            break
