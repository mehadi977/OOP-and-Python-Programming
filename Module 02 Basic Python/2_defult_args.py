# def sum_(num1,num2,num3):
#     sum=num1+num2+num3
#     return sum

# ans=sum_(2,4,3)
# print(ans)

# def sum_(num1,num2,num3=0):
#     sum=num1+num2+num3
#     return sum

# ans=sum_(2,4)
# print(ans)

#args
# variable number of arguments
def all_sum(num1,num2,*args):
    print(args)
    sum=0
    for num in args:
        sum+=num
    return sum

    
allsum = all_sum(4,1,5,2,6,6,3,2,5)
print(allsum)