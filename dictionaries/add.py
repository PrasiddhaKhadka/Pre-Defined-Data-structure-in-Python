thisdict ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Add a new item to the original dictionary
thisdict["color"] = "red"

# Add a new item using update method
thisdict.update({"engine":"V8"})

print(thisdict)