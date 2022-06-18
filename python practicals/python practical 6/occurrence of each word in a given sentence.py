#6.Program to count the occurrence of each word in a given sentence
a = list(map(str,input("Enter the sentence ").split()))
s = set(a)
for i in s:
    print(i,"occures",(a.count(i)),"times")