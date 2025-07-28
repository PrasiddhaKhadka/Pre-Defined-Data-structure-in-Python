thisdict ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Change the "year" value from 1964 to 2020
thisdict['year'] = 2020

# Change using update method
thisdict.update({"year": 2024})

print(thisdict)