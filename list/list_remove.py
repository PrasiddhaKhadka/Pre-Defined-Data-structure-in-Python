
# remove a specific item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# remove the first item
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# remove the last item
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.pop() || item = thislist.pop()
# print(item)
print(thislist)


# remove the specified index
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop(1)
print(thislist)


# del keyword
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
del thislist[0]
print(thislist)


# clear the list
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.clear()
print(thislist)



# 🥳 Note (Difference between Pop and del)