class User:
    def __init__(self,email, age, address) -> None:
        # it is ram.email = email (so that each instance is unique here)
        self.email = email
        # global can me used to make it access but will not be unqiue 
        global myname
        myname = email

        self.age = age
        self.address = address

    def __str__(self) -> str:
        return f'My email is {self.email} and I am {self.age}, I live in {self.address} & my name is testing {myname}'



# we'r not passing the self here 
ram = User('ram@gmail.com',27,'Pokhara')
# when we create a instance here now our self become ram
shyam = User("shyam@gmail.com", 30, "Kathmandu")



print(ram)
print(shyam)

'''
Will print same as the global scope variable will not be unqiue here
'''
