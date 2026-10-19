name ='Mehadi\'s Hasan' #escape korar jonno \  
name2="Tasnia Raicha"
# multiline string
name3= """ 
    Mehadi Hasan 
    Shanto
"""
print(name)

# string is a sequence of characters
for char in name2:
    print(char)
print(name2[3])
print(name2[7:13])
print(name2[-3])
print(name2[::-1])
# mutable means changeable

# immutable means yoy can not change it
# name2[0]='R' #no change
print(name2)
if 'Raicha' in name2:
    print('ache')
else: 
    print('nai')
print(name2.upper())