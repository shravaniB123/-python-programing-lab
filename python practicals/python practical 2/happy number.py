#1.Write a python program to check if the given number is Happy Number
def Happy(n):
    rem = sum = 0
    while n>0:
        rem = n%10
        sum = sum +(rem*rem)
        n = n//10
    return sum 
n = 129
res = n
while(res!=1 and res!=4):
    res = Happy(res)
if(res==1):
    print("n is happy number")
elif(res==4):
    print("n is not a happy number")



