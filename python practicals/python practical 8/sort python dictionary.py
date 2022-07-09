#1. Sort python dictionary by key and value
dict = {'aman':12,
	    'rajesh':10,
		'ram':27,
		'madhuri':13}

print("Sorted by key:")
print(sorted(dict.items(),key=lambda kv:(kv[0], kv[1])))

print("\nSorted by value:")
print(sorted(dict.items(), key=lambda kv: (kv[1], kv[0])))
