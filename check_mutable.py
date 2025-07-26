mylist = [1, 2, 3]
print(id(mylist))      
mylist.append(4)
print(mylist)
print(id(mylist))      # Same ID → mutable

print("----------------")

s = "hello"
print(id(s))           
s += " world"
print(s)
print(id(s))           # Different ID → immutable
