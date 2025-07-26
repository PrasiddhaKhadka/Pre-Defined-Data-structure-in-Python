thislist = list(("apple", "banana", "cherry","mango","grapes")) 

# will access the first element 
print(thislist[::2])

# will access the last element
print(thislist[-1])

# will access the 2nd to 4th element
print(thislist[2:8])

# will access the first 4 elements
print(thislist[:4])

# will access the 2nd element and onwards
print(thislist[2:])

# will access the last 3 elements
print(thislist[-4:-1])

# will check if "apple" is present in the list
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")