thisdict={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


# Remove the "model" key from the dictionary
thisdict.pop("model")
print(thisdict)


# Remove the last key and its value from the dictionary
thisdict.popitem()
print(thisdict)


# clear the dictionary
thisdict.clear()
print(thisdict)


# delete the dictionary
del thisdict


