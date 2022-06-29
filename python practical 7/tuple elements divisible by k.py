#6. Python program to find tuples which have all elements divisible by k
t_list = [(6,24,12),(7,9,6),(12,18,21)]
print("The original list is: "+str(t_list))
k = 6
res = [sub for sub in t_list if all(ele %k == 0 for ele in sub)]
print("k multiple elments tuples: "+str(res))