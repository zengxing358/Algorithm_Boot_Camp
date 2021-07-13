import heapq
a=input()
arr=a.split()
temp=[int(i) for i in arr if i!="x" ]
cnt=0
def mergesort(nums):
    global cnt
    n=len(nums)
    if n<=1:
        return nums
    mid=n>>1
    left=mergesort(nums[:mid])
    right=mergesort(nums[mid:])
    res=[]
    i,j=0,0
    l=len(left)
    r=len(right)
    while i<l and j<r:
        if left[i]>right[j]:
            cnt+=l-i
            j+=1
        else:
            i+=1
    i,j=0,0
    while i<l and j<r:
        if left[i]>right[j]:
            res.append(right[j])
            j+=1
        else:
            res.append(left[i])
            i+=1
    if i<l:
        res+=left[i:]
    if j<r:
        res+=right[j:]
    return res
mergesort(temp)
def getval(arr):
    res=0
    for i in range(9):
        if arr[i]!="x":
            t=int(arr[i])-1
            res+=abs(t//3-i//3)+abs(t%3-i%3)
    return res
if cnt%2==1:
    print(-1)
else:
    dist={}
    pre={}
    heap=[]
    end="12345678x"
    start="".join(arr)
    dist[start]=0
    heapq.heappush(heap,(getval(start),start))
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    op="urdl"
    while heap:
        t=heapq.heappop(heap)
        source=t[1]
        step=dist[source]
        if source==end:
            print(step)
            break
        state=list(source)
        k=state.index("x")
        x=k//3
        y=k%3
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<3 and ny>=0 and ny<3:
                state[x*3+y],state[nx*3+ny]=state[nx*3+ny],state[x*3+y]
                nxt="".join(state)
                if nxt not in dist or dist[nxt]>step+1:
                    dist[nxt]=step+1
                    pre[nxt]=(source,op[i])
                    heapq.heappush(heap,(getval(nxt)+dist[nxt],nxt))
                state[x*3+y],state[nx*3+ny]=state[nx*3+ny],state[x*3+y]