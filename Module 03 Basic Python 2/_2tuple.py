def multiple():
    return 2,5
print(multiple())

things='pen','book','phone','charger','brush'
print(things)
print(type(things))
print(things[2])
print(things[-2])
print(things[2:4])

for item in things:
    print(item)

# things[0]='bus' #no change in touple

mega =([2,3,5], [1,7,2],[3,4])
print(mega[1])
mega[1][0]=777
print(mega[1])