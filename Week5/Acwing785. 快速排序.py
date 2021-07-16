import random
def quicksort(arr,start,end):
    if start>=end:
        return
    r=random.randint(start,end-1)
    arr[start],arr[r]=arr[r],arr[start]
    s=arr[start]
    cur=start+1
    right=end
    mid=start
    while cur<right:
        if arr[cur]<s:
            mid+=1
            arr[cur],arr[mid]=arr[mid],arr[cur]
            cur+=1
        elif arr[cur]==s:
            cur+=1
        else:
            right-=1
            arr[cur],arr[right]=arr[right],arr[cur]
    arr[mid],arr[start]=arr[start],arr[mid]    
    quicksort(arr,start,mid)
    quicksort(arr,right,end)

n=int(input())
b=input()
arr=[int(i) for i in b.split()]
quicksort(arr,0,n)
print(" ".join([str(i) for i in arr]))