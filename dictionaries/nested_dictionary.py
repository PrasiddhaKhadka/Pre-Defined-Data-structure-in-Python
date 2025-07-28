thisdictionary ={
    "name":"Ram",
    "age":25,
    "address":{
        "city":"Pokhara",
        "country":"Nepal"
    },
    "email":"ram123@gmail.com",

}

print(thisdictionary['address']['city'])

for key in thisdictionary["address"]:
    print(key, ":", thisdictionary["address"][key])

for key, value in thisdictionary.items():
    print(key, ":", value)

for keys in thisdictionary.keys():
    print(keys)