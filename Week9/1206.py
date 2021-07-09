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
        for head,tail in zip(self.heads,self.tails):
            head.right=tail
        for up,down in zip(self.heads,self.heads[1:]):
            up.down=down

    def search(self, target: int) -> bool:
        cur=self.heads[0]
        while cur:
            if cur.val<target and cur.right.val>target:
                cur=cur.down
            elif target==cur.right.val:
                return True
            else:
                cur=cur.right
        return False

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
            if random.randint(0,1):
                break

    def erase(self, num: int) -> bool:
        cur=self.heads[0]
        frag=False
        while cur:
            if cur.val<num and cur.right.val>=num:
                if cur.right.val==num:
                    cur.right=cur.right.right
                    frag=True
                cur=cur.down
            else:
                cur=cur.right
        return frag