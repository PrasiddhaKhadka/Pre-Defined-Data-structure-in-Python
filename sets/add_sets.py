# add an element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)


# add multiple elements to the set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


# update the set by adding elements from another List : Not Necessary to be a set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)