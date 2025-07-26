# join using + operator

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# join using append()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# join using extend()

list1 = ["a", "b" , "c"]
list2 = ["d","e","f"]
print(list1.count("b"))

list1.extend(list2)
print(list1)