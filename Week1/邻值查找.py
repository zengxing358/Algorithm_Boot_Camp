n=int(input())
b=input()
lst=b.split()

class Node:
    def __init__(self,val,key,pre=None,next=None):
        self.val=val
        self.key=key
        self.pre=pre
        self.next=next
        
lst=[(idx,int(val)) for idx,val in enumerate(lst)]
lst.sort(key=lambda x:x[1])
head=Node(-float("inf"),-2)
tail=Node(float("inf"),-1)
dic={}
cur=head
for idx,val in lst:
    newNode=Node(val,idx,cur)
    cur.next=newNode
    dic[idx]=newNode
    cur=cur.next
cur.next=tail
tail.pre=cur
res=[0]*(n-1)
for i in range(n-1,0,-1):
    node=dic[i]
    left=node.val-node.pre.val
    right=node.next.val-node.val
    if left<=right:
        res[i-1]=[left,node.pre.key+1]
    else:
        res[i-1]=[right,node.next.key+1]
    node.next.pre=node.pre
    node.pre.next=node.next
for v,k in res:
    print(v,k)