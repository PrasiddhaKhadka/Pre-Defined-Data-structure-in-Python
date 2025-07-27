weekTuple = ("Sunday", "Monday", "Tuesday", 
             "Wednesday", "Thursday", "Friday")

x = list(weekTuple)
x.append("Saturday")

weekTuple = tuple(x)

print(weekTuple)



# Adding tuple with tuple

myFruits = ("apple", "banana", "cherry")
myTropical = ("kiwi", "pineapple", "papaya")
myFruits += myTropical
print(myFruits)