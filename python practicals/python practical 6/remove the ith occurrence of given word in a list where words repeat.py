#3. Program to remove the ith occurrence of given word in a list where words repeat
def omit(l1,w,n):
    c = 0 
    idx = 0
    for i in l1:
        idx+=1 
        if i==w:
            c+=1 
            if c==n:
                l1.pop(idx-1)
    return l1 

l1 = ["The","boy","is","smart","he","is","intelligent","he","is","silent"]
w = "is"
n = 2
print("New list is:",omit(l1,w,n))