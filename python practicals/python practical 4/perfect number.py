#1. Python program to print perfect number
N = int(input("Enter a number:"))
sum = 0
for i in range(1,N):
    if N%i==0:
        sum = sum + i 
if sum==N:
    print(N,"is a perfect number")
else:
    print(N,"is not a perfect number")
