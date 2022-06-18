#1. Python program to find the length of list using recurrence
def length(num):
    if not num:
        return 0
    return 1 + length(num[1::2]) + (length(num[2::2]))
num = [1,2,3]
print("Length of string is: ")
print(length(num))