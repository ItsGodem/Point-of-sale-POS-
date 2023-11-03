import json
product = []
    
filename2 = "app/product.json"
with open(filename2, "r+") as file:
    data = json.load(file)
    for x in data:
        product.append(x)
users=[]
filename = "app/users.json"
with open(filename, "r+") as file:
    data = json.load(file)
    for x in data:
        users.append(x)
