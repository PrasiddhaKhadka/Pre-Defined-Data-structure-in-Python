mytodoList = []

user_input = [input("Contact Name: "),input("Contact Number: ")]

mytodoList.append(user_input)

found = False

# searching the number of elements in the list
for contacts in mytodoList:
    if "Aman" in contacts:
        print("Contact Name: ", contacts[0])
        print("Contact Number: ", contacts[1])
        found = True
        break

if not found:
    print("Contact not found")


mytodoList.remove(user_input)