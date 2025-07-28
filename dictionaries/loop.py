thisdict ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for key in thisdict:
    print(key)

# get keys
for value in thisdict.keys():
    print(value)

# get values
for value in thisdict.values():
    print(value)

# get keys and values
for key, value in thisdict.items():
    print(key, value)