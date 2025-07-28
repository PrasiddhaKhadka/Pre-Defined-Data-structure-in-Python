thisdict ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# copy using copy method
newdict = thisdict.copy()

# copy using dict constructor
mydict = dict(thisdict)

print(newdict)