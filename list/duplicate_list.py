# duplicate a list
list1 = ["apple", "banana", "cherry", "apple", "cherry"]
list2 = list1.copy()
print(list2)


# duplicate a list using constructor of list()
list1 = ["apple", "banana", "cherry", "apple", "cherry"]
list2 = list(list1)
print(list2)


# duplicate a list using slice operator
list1 = ["apple", "banana", "cherry", "apple", "cherry"]
list2 = list1[1:4]
print(list2)


# 🐶 Not to do 
list1 = ["apple", "banana", "cherry", "apple", "cherry","grapes"]
list2 = list1
print(list2)