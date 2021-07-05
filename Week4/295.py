class Node:
    def __init__(self,val,dtype):
        self.val=val
        self.type=dtype
    def __lt__(self,other):
        if self.type=="min":
            return self.val<other.val
        return self.val>other.val
    def __gt__(self,other):
        if self.type=="min":
            return self.val>other.val
        return self.val<other.val

class Heap:
    def __init__(self,dtype):
        self.type=dtype
        self.heap=[]
        self.size=0
    def push(self,val):
        new=Node(val,self.type)
        self.heap.append(new)
        self.up(self.size)
        self.size+=1
    def up(self,index):
        if index:
            parent=(index-1)//2
            if self.heap[parent]>self.heap[index]:
                self.swap(parent,index)
                self.up(parent)
    def swap(self,p,q):
        self.heap[p],self.heap[q]=self.heap[q],self.heap[p]
    def down(self,index):
        left=index*2+1
        right=index*2+2
        frag=index
        if left<self.size and self.heap[left]<self.heap[frag]:
            frag=left
        if right<self.size and self.heap[right]<self.heap[frag]:
            frag=right
        if frag!=index:
            self.swap(frag,index)
            self.down(frag)
    def pop(self):
        if self.size:
            res=self.heap[0].val
            self.size-=1
            if self.size:
                self.heap[0]=self.heap.pop()
                self.down(0)
            else:
                self.heap.pop()
            return res
    def top(self):
        if self.size:
            return self.heap[0].val
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min=Heap("min")
        self.max=Heap("max")
        self.size=0

    def addNum(self, num: int) -> None:
        if self.size:
            if num>self.findMedian():
                self.min.push(num)
                if self.min.size>self.max.size+1:
                    self.max.push(self.min.pop())
            else:
                self.max.push(num)
                if self.max.size>self.min.size+1:
                    self.min.push(self.max.pop())
        else:
            self.max.push(num)
        self.size+=1
    def findMedian(self) -> float:
        if self.size:
            if self.size%2==0:
                return (self.min.top()+self.max.top())/2
            if self.min.size>self.max.size:
                return self.min.top()
            return self.max.top()