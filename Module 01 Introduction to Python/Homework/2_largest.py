a=int(input('Enter the 1st num: '))
b=int(input('Enter the 2nd num: '))
c=int(input('Enter the 3rd num: '))
if a>b and a>c:
    print("Largest number is a: ",a)
elif b>c :
    print("Largest number is b: ",b)
else :
    print("Largest number is c" ,c)
# in one function 
print(max(a,b,c))