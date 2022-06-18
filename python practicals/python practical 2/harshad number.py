#5.Write a python program to determine whether the given number is a Harshad number
#If a number is divisible by the sum of its digits, then it will be known as Harshad number
N = int(input("Enter a number:"))
sum = 0
for i in str(N):
    sum = int(i)
if N%sum==0:
    print(N,"is a Harshad number")
else:
    print(N,"is not a Harshad number")