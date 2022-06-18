#3.Write a python program to check if the given number is Disarium Number
num = 89
rem = s = 0
len = len(str(num))
n = num
while(num>0):
    rem = num%10
    s = s + int(rem**len)
    num = num//10
    len = len-1
if(s==n):
    print("Given number is Disarium")
else:
    print("Given number is not a Disarium")