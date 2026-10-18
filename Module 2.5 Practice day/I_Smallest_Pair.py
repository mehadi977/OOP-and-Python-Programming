# Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/I
tst=int(input())
for tc in range(tst):
    n=int(input())
    arr=[]
    arr= list(map(int,input().split()))
    ans=1e7
    # print(arr)
    # print(ans)
    for i in range(n):
        for j in range(i+1,n): 
            # if i!=j:
            ans=min(ans,(arr[i]+arr[j]+j-i))
                
    print(ans)
    
    
    