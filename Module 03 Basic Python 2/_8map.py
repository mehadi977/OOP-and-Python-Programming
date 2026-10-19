double= lambda num:num*2

nums=[12,43,2,6,7,2,7,22,10]
# doubled_nums=map(double,nums)
doubled_nums=map(lambda num:num*2,nums)
print(nums)
print(list(doubled_nums))

squrad_nums=map(lambda x:x*x,nums)
print(list(squrad_nums))

actors=[
    {'name': 'walter white', 'age': 50},
    {'name': 'jessy ', 'age': 25},
    {'name': 'Hank', 'age': 45},
    {'name': 'Gus', 'age': 42},
    ]
juniors=filter(lambda act:act['age']<45,actors)
fivers=filter(lambda act:act['age']%5==0,actors)
print(list(juniors),'\n')
print(list(fivers))
