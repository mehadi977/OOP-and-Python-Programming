lst=[1,4,7,33,6,75,24,73,70,90,85,50,45]
# print(lst)
odds=[]
for num in lst :
    if num%2==1 and num%5==0:
        odds.append(num)
print(odds)

# odds2=[num for num in lst if num%2==1]
odds2=[num for num in lst if num%2==1 if num %5==0]
print(odds2)

# nested loop
player=['khalid','mamun','abid']
number= [12,10,15]
all_combanition=[]
for name in player:
    # print(name)
    for num in number:
        # print(name,num)
        all_combanition.append([name,number])
        
print(all_combanition,'\n')