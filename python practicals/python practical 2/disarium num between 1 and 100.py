#4.Write a python program to print all disarium numbers between 1 and 100
def calculatelength(n):
    l = 0
    while(n!=0):
        l = l + 1
        n = n//10
    return l
def sumofDigits(num):
    rem = sum =0
    len = calculatelength(num)
    while(num>0):
        rem = num%10
        sum = sum + int(rem**len)
        num = num//10
        len = len-1
    return sum
result = 0
print("Disarium numbers between 1 and 100 are:")
for i in range(1,101):
    result = sumofDigits(i)
    if(result==i):
        print(i)