
# function is a first class object
def double_decker():
    print('Starting double decker')
    def inner_functn():
        print('inside the inner')
        return 2323
    return inner_functn

print(double_decker())
print(double_decker()())

def do_something(work):
    print('start work')
    # print(work)
    work()
    print('end word')
    
def coading():
    print('coading python')
    

# do_something(4)
# do_something('coading')
# do_something('coading')

do_something(coading)

def sleeping():
    print('sleeping and dreaming')
    
do_something(sleeping)