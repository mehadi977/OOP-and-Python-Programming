def fullname(fst,lst):
    name = f'Full name is: {fst} {lst}'
    return name

fast_name='Tasnia'
last_name='Raicha'
# nam=fullname(fast_name, last_name)
# print(nam)
nm=fullname(lst=last_name,fst=fast_name)
print(nm)


# kargs key value akare value rakhe
def famus_name(fst,lst,**kargs):
    name=f'{fst},{lst}'
    print(fst,lst)
    # print(kargs['title'])
    for key,val in kargs.items():
        print(key,val)
    
name=famus_name(fst='Mehadi',lst='Hasan',title='Santo', tile2='from',last2='Rajbari')

# return multiple things in pyton
def a_lot(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    rem=a%b
    return sum,sub,mul,div,rem
    # return [sum,sub,mul,div,rem]

everithing=a_lot(5,2)
print(everithing)