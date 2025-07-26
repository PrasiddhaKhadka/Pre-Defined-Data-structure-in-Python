# remove an item
# why? remove method will raise an error if the specified item does not exist
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


# remove an item using discard method
# why? discard method will not raise an error if the specified item does not exist
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


# remove an item using pop method
# why not to use pop? pop method will remove a random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


# clear the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


# delete the set
thisset = {"apple", "banana", "cherry"}
del thisset
# throw an error because the set no longer exists
# print(thisset)