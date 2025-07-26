# sort the list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# reverse the order of the list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.reverse()
print(thislist)


# sort the list alphabetically in descending order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)



# Case Insensitive -> Output ['Kiwi', 'Orange', 'banana', 'cherry']
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Case Insensitive -> Output ['banana', 'cherry', 'Kiwi', 'Orange']
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)



def myfunc(n):
  # absolute value (always positive)
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23] 
# [100 (50) | 50 (0) | 65 (15) | 82 (32)| 23 (27) |]
thislist.sort(key = myfunc)
# [50 (0) | 65 (15) | 23 (27) | 82 (32)| 100 (50) |]
print(thislist)