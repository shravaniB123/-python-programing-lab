#2.Python program to convert decimal to binary
print("Enter decimal number:")
num = int(input())
b = 0
mul = 1
while num>0:
    rem = num%2
    b = b + (rem*mul)
    mul = mul*10
    num = int(num/2)
print("Equivalent binary value:",b)