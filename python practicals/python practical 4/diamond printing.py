#5. Python program for diamond printing
num = 4
s = num-1
for i in range(1,num+1):
    for j in range(1,s+1):
        print(end=" ")
    s = s-1
    for j in range(2*i-1):
        print(end="*")
    print()
s = 1
for i in range(1, num):
    for j in range(1, s+1):
        print(end=" ")
    s = s+1
    for j in range(1, 2*(num-i)):
        print(end="*")
    print()