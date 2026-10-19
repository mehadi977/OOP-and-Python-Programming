numbers=[12,31,34,11,44,22]
parson1=['Mehadi','Dhaka',21,'Student']
# key value pair
# dictionary
# object
# hash table 
# overlap with set

# dictonary:
parson= {'name': 'Mehadi', 'address': 'Dhaka', 'age':21,'job': 'bekar' }
print(parson1)
print(parson)
print(parson['age'])
print(parson.keys()) #sudhu key
print(parson.values()) #only vlau
parson['languege']='python' #add key vlaue
parson['name']='Mehadi Hasan'
print(parson)
del parson['age']
print(parson)

for key,val in parson.items():
    print(key,val)