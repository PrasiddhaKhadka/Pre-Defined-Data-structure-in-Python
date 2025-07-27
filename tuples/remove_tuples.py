weekTuple = ("Sunday", "Monday", "Tuesday", 
    "Wednesday", "Thursday", "Friday")

del weekTuple


# print(weekTuple)


# Remove tuple by converting it to a list

weekTuple = ("Sunday", "Monday", "Tuesday", 
    "Wednesday", "Thursday", "Friday")

x = list(weekTuple)

x.remove("Monday")

weekTuple = tuple(x)

print(weekTuple)
