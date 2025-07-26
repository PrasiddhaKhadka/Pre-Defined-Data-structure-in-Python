# join using union
set1 = {1, 2, 3}
set2 = {1, 2, 4}

set3 = set1.union(set2)
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


# join using update()
set1 = {1, 2, 3}
set2 = {1, 2, 4}

set1.update(set2)
print(set1)



# join using | pipe operator or bitwise operator
set1 = {1, 2, 3}
set2 = {1, 2, 4}
set3 = {5, 6, 7}

set4 = set1 | set2 | set3
print(set4)



# intersection 
set1 = {1, 2, 3}
set2 = {1, 2, 4}
set3 = {2, 6, 7}

set4 = set1.intersection(set2, set3)
# also can intersect with & => set4 = set1 & set2 & set3

print(set4)


# difference
set1 = {1, 2, 3}
set2 = {1, 2, 4}
set3 = {2, 6, 7}

set4 = set1.difference(set2, set3)
print(set4)


# symmetric difference
set1 = {1, 2, 3}
set2 = {1, 2, 4}

set3 = set1.symmetric_difference(set2)
print(set3)