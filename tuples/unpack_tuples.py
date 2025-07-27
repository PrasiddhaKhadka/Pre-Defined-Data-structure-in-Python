# Using Foor in loop
fruits = ("apple", "banana", "cherry")

for x in fruits:
    print(x)


# Assigning a variable
fruits = ("apple", "banana", "cherry")
(a, b, c) = fruits
print(a)
print(b)
print(c)

# Assigning with a Asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "kiwi")
(a, b, *c) = fruits
print(a)
print(b)
print(c)