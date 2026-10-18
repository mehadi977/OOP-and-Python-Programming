#swap min max val in an array
n=int(input())

arr=list(map(int,input().split())) #array input

    
# print(arr)

mx=max(arr)
mn=min(arr)
# print(mx,mn)
# for i in range(len(arr)):
#     if arr[i]==mx:
#         arr[i]=mn
#     elif arr[i]==mn:
#         arr[i]=mx

mx_idx=arr.index(max(arr))
mn_idx=arr.index(min(arr))
# print(arr)
tmp=arr[mx_idx]
arr[mx_idx]=arr[mn_idx]
arr[mn_idx]=tmp
        
print(*arr)
