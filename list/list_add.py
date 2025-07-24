
# add an element to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# add an element at the specified index and shift the existing elements
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# add elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# add elements from a tuple to the current list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)