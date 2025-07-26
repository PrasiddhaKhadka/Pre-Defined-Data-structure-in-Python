fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist =[]

for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [expression for item in iterable if condition == True] 😇
newlist = [ x.upper() for x in fruits if "a" in x ]

print(newlist)


# Expression Syntax