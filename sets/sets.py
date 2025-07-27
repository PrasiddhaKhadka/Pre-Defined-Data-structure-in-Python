myset = {'apple', 'banana', 'cherry'}

# will return the data type
print(type(myset))
# will return the length
print(len(myset))
# might print the myset in any ordered format
print(myset)



fruitset = {"apple", "banana", "cherry", "apple", "cherry"}
# will only print unique values (no duplicates)
print(fruitset)
thisset = {"apple", "banana", "cherry", True, 1, 2}
# True and 1 are considered the same value
# False and 0 are considered the same value
print(thisset)


# creating a set using a constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)




# GOOD FOR CONSTANT VALUES ONLY LIKE COLORS, EMAIL