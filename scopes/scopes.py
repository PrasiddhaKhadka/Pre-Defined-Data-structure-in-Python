# Global scope
player_health = 10

def def_drink():
    # local scope
    potion_strength = 2

    # to make global 
    global new_var
    new_var = 5
    print(f'The playe potion strength is {potion_strength}')
    print(f'The player health is {player_health}')


def_drink()
# calling of function is necesaary ok !
print(new_var)



# incase the variable is define inside the if loop it wont be the global scope:
# if .... :
     # var = jdjjj

# can be called here printing (var)