# list,array,collection is same

# index:  0  1  2  3  4  5  6  7
numbers= [4, 6, 3, 2, 7, 9, 2, 9]
# index:  -8 -7 -6 -5 -4 -3 -2 -1
print(numbers[0])
print(numbers[7])
print(numbers[1])
print(numbers[-1])
print(numbers[-8])
# list(start:end)== start from the start index and stop before the end index
print(numbers[2:5]) #print index 2,3,4
print(numbers[-1:-5])
print(numbers[0:5:1]) #increse by 1
print(numbers[0:5:2]) #increse by 2
# ulta dike print
print(numbers[6:2:-1])
print(numbers[6:2:-2])
print(numbers[4:]) #4 index theke ses porjunto
print(numbers[:5]) # 0 index theke 4index porjunto
print(numbers[:]) #shob print korbe
print(numbers[::-1]) #reverse printing(sortcut to revers arry list)