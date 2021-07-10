n=int(input())
temp=input()
lst=[int(i) for i in temp.split()]
lst.sort()
t=lst[n//2]
res=0
for i in range(n):
    res+=abs(lst[i]-t)
print(res)