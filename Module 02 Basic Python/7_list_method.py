lst=[6,2,8,4]
print(lst)
for val in lst:
    print(val)
    
lst.append(55)
print(lst)
lst.insert(1,33)
print(lst)
if 9 in lst:
    lst.remove(9)
print(lst)
if 6 in lst:
    lst.remove(6)
print(lst)
lst.pop()
print(lst)
a=lst.pop()
print(a,lst)
if 2 in lst:
    idx_a_val= lst.index(2)
print(idx_a_val)
lst.append(5)
lst.append(13)
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True) #reverse sort
print(lst)
lst.reverse()
print(lst)