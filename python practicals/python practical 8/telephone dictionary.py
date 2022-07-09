#4. Write telephone dictionary of 10 students using dictionary and perform operations
def find_num(name):
    print(name,":",d[name])

def replace_num(name,num):
    d[name] = num 
    print("Contact updated\n", name, ":", d[name])

def replace_name(name, num):
    for key, value in d.items():
        if num == value:
            d[name] = d[key]
            del d[key]
            break 
    print("Contact updated!\n", name, ":", d[name])

d = {"Mirabel": 9101443214,
     "Isabel": 9325544335,
     "Bruno": 7853232315,
     "Luisa": 9446583852}

find_num("Bruno")
replace_num("Luisa", 8632436547)
replace_name("Esha", 9325544335)