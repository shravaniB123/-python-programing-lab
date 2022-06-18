#6.Python program to print left aligned number pattern
print("Pattern of numbers:")
n = 1
for i in range(9):
    for j in range(i+1):
        print(n, end=" ")
        n = n + 1 
    print()