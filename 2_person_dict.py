person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print(person['children'][1])

print(person['pets'][1])

for child in person['children']:
    print(child)

for p in person['pets']:
    print(person['pets'][p])