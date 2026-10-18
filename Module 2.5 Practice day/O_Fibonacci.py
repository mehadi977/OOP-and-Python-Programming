n=int(input())
a=0
b=1

for i in range(1,n):
    a,b = b,a+b
    
print(a)