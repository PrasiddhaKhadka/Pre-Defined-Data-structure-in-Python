fruits =[ "apple", "banana", "cherry", "kiwi", "mango"]

for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i])


thislist = ["apple", "banana", "cherry"]

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


thislist = ["apple", "banana", "cherry"]
[print(x+" is a fruit") for x in thislist]