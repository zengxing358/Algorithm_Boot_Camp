# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Heap:
    def __init__(self):
        self.heap=[]
        self.size=0
    def push(self,val):
        self.heap.append(val)
        self.up(self.size)
        self.size+=1
    def pop(self):
        if self.size:
            res=self.heap[0]
            self.size-=1
            if self.size:
                self.heap[0]=self.heap.pop()
                self.down(0)
            else:
                self.heap.pop()
            return res
    def up(self,index):
        if index:
            parent=(index-1)//2
            if self.heap[parent]>self.heap[index]:
                self.swap(parent,index)
                self.up(parent)
    def down(self,index):
        left=index*2+1
        right=index*2+2
        Min=index
        if left<self.size and self.heap[left]<self.heap[Min]:
            Min=left
        if right<self.size and self.heap[right]<self.heap[Min]:
            Min=right
        if Min!=index:
            self.swap(Min,index)
            self.down(Min)
    def swap(self,p,q):
        self.heap[p],self.heap[q]=self.heap[q],self.heap[p]
    def isempty(self):
        return self.size==0
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap=Heap()
        for lis in lists:
            while lis:
                heap.push(lis.val)
                lis=lis.next
        s=ListNode(49)
        cur=s
        while not heap.isempty():
            cur.next=ListNode(heap.pop())
            cur=cur.next
        return s.next