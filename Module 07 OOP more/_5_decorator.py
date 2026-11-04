import math
def timer(funcn):
    def inner(*args, **kwrgs):
        print('time started')
        print(funcn)
        funcn(*args,**kwrgs)
        print('time ended')
    return inner

# print(timer()())

@timer
def get_factrial(n):
    print('factorial statring')
    result=math.factorial(n)
    print(f'factorial of {n} is: {result}')
    
    
# get_factrial(timer)

# complex way to decorate
# timer(get_factrial)()

get_factrial(5)

