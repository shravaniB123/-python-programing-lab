a = list(map(str,input("Enter the elements of the list").split()))
w = input("Enter a word")
c = 0 
for i in a:
    if i==w:
        c+=1 
print(c)