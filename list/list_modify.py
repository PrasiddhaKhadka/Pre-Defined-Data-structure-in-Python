thislist = ["apple", "banana", "cherry"]

# will replace "banana" with "blackcurrant"
thislist[1] = "blackcurrant"

# will replace "banana" and "cherry" with "blackcurranty" and "watermelon"
thislist[1:3] = ["blackcurranty", "watermelon"]

# will insert "watermelon" before "cherry"
thislist.insert(2, "watermelon")

print(thislist)