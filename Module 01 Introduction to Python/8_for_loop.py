arr=[3,5,7,2,5,9,1]

sum=0
for num in arr:
    print(num) 
    sum+=num
    print('sum is: ',sum)

print(sum)

txt='Hello'
for char in txt:
    print(char)
    
# range(start,end,increment or decrement)
for i in range(1,10,2):
    print(i)
    
topic= ['Data','Algo','DSA', 'Python','C++','Jave']
for idx, all in enumerate(topic):
    # print(idx)
    print(idx,all)