# set: unique item collection
# list = []
# tuple = ()
# set = {}
numbers=[23,8,8,7,2,3,5,8,2,4,3]
print(numbers)
numbers_set=set(numbers)
print(numbers_set)
numbers_set.add(999)
print(numbers_set)
numbers_set.remove(8)
print(numbers_set)
# print(numbers_set[2]) #evabe acces kora jabe na

for item in numbers_set:
    print(item)
    
if 9 in numbers_set:
    print('9 exists')
elif 7 in numbers_set:
    print('7 exist')
    
# Union
A={1,3,9}
B={1,2,3,4,5}
print(A&B) #A intersecton B
print(A|B) #A union B
