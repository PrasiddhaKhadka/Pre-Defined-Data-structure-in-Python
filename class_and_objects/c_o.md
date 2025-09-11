# Understanding `self`, Local Variables, and Global Variables in Python Classes

In Python, when working with classes, we often get confused about when to use:

1. **Local variables (just names inside a function)**  
2. **Instance variables (using `self`)**  
3. **Global variables (`global`)**

This guide shows the difference with clear examples and outputs.

---

## Example: Comparing All Three Approaches

### 1. Using Only Local Variables (❌ Wrong for Objects)

```python
class User:
    def __init__(self, email, age, address):
        email = email        # local variable
        age = age            # local variable
        address = address    # local variable

ram = User("ram@gmail.com", 27, "Pokhara")
print(ram.email)   # ❌ Error

Output:

AttributeError: 'User' object has no attribute 'email'


⚠️ Here, email, age, and address exist only inside the __init__ method.
They are temporary variables and disappear once the method finishes.

--


2. Using self (✅ Correct Way)

class User:
    def __init__(self, email, age, address):
        self.email = email      # stored inside the object
        self.age = age
        self.address = address

    def __str__(self):
        return f"My email is {self.email}, I am {self.age}, and I live in {self.address}"

ram = User("ram@gmail.com", 27, "Pokhara")
shyam = User("shyam@gmail.com", 30, "Kathmandu")

print(ram)
print(shyam)


Output:

My email is ram@gmail.com, I am 27, and I live in Pokhara
My email is shyam@gmail.com, I am 30, and I live in Kathmandu


✅ Each object has its own data, stored in self.

--

3. Using Global Variables (⚠️ Shared by All)
class User:
    def __init__(self, email, age, address):
        self.email = email        # instance attribute
        global myname
        myname = email            # global variable (shared)

        self.age = age
        self.address = address

    def __str__(self):
        return (f"My email is {self.email}, I am {self.age}, "
                f"I live in {self.address} & my name is testing {myname}")

ram = User("ram@gmail.com", 27, "Pokhara")
shyam = User("shyam@gmail.com", 30, "Kathmandu")

print(ram)
print(shyam)


Output:

My email is ram@gmail.com, I am 27, I live in Pokhara & my name is testing shyam@gmail.com
My email is shyam@gmail.com, I am 30, I live in Kathmandu & my name is testing shyam@gmail.com


⚠️ Notice that even when printing ram, the global variable myname has been overwritten by shyam.
This shows that global variables are shared across all objects.

--

``Key Takeaways``

Local variables: Temporary, exist only inside the function → ❌ not useful for objects.

self (instance variables): Data is stored in the object → ✅ correct, each instance is unique.

Global variables: Shared across all instances → ⚠️ not suitable for per-object data.