import random
class Node:
    def __init__(self,val,right=None,down=None) -> None:
        self.val=val
        self.right=right
        self.down=down
class Skiplist:
    def __init__(self):
        self.heads=[Node(-float("inf")) for _ in range(16)]
        self.tails=[Node(float("inf")) for _ in range(16)]
        self.frag=self.tails[-1]
        self.max=-1
        for head,tail in zip(self.heads,self.tails):
            head.right=tail
        for up,down in zip(self.heads,self.heads[1:]):
            up.down=down

    def add(self, num: int) -> None:
        stack=[]
        cur=self.heads[0]
        while cur:
            if cur.val<num and cur.right.val>=num:
                stack.append(cur)
                cur=cur.down
            else:
                cur=cur.right
        down=None
        while stack:
            cur=stack.pop()
            node=Node(num,cur.right,down)
            cur.right=node
            down=node
            if node.right==self.frag:
                self.max=node.val
            if random.randint(0,1):
                break
    def findMax(self):
        return self.max

    def erase(self, num: int) -> bool:
        cur=self.heads[0]
        frag=False
        while cur:
            if cur.val<num and cur.right.val>=num:
                if cur.right.val==num:
                    if cur.right.right==self.frag:
                        self.max=cur.val
                    cur.right=cur.right.right
                    frag=True
                cur=cur.down
            else:
                cur=cur.right
        return frag
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        temp=Skiplist()
        res=[]
        for i in range(len(nums)):
            temp.add(nums[i])
            if i>=k-1:
                res.append(temp.findMax())
                if i!=len(nums)-1:
                    temp.erase(nums[i-k+1])
        return res