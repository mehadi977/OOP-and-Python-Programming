# Problem Link: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/N
a,b=map(int,input().split())

# print(a,b)
s=input()
fst=False
if s[a]=='-':
    fst=True
secnd=True
for i in range(len(s)):
    if i==a:
        continue
    
    if not(s[i]>='0' and s[i]<='9') :
   
        secnd=False
        break

if fst==True and secnd==True :
    print("Yes")
else:
    print("No")
# print(s)