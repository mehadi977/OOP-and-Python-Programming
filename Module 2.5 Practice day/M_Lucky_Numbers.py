a,b=map(int, input().split())  #eki line er input nite
# print(a,b)
ans=[]
def check_its_lucky(n):
    s=str(n)
    flag=True
    for c in s:
        # if c=='4' or c== '7':
        #     flag=True
        # else:
        #     flag=False
        #     break
        if c not in '47':
            flag=False
    if flag==True:
        ans.append(n)
            
        

for i in range(a,b+1):
    # print(i)
    check_its_lucky(i)
    
if len(ans)==0:
    print(-1)
else :
    print(*ans)