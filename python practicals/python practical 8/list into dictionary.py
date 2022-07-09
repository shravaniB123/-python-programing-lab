#3. Take two list as input and convert them into dictionary and print dictionary 
combined_dict = {}
keys = ["k1","k2","k3","k4"]
values = ["v1","v2","v3","v4"]

for k,v in zip(keys,values):
    combined_dict[k] = v 

print(combined_dict)