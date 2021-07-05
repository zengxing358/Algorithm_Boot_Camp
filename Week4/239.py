class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
    def __lt__(self,other):
        return self.value<other.value
    def __eq__(self,other):
        return self.value==other.value
    def __gt__(self,other):
        return self.value>other.value
class MaxHeap:
    def __init__(self):
        self.heap=[]
        self.dic={}
        self.size=0
    def add(self,node):
        if self.heap:
            self.heap.append(node)
            self.dic[node.key]=self.size
            self.up(self.size)
            self.size+=1
        else:
            self.heap.append(node)
            self.dic[node.key]=self.size
            self.size+=1
    def getMax(self):
        return self.heap[0].value
    def replaceNode(self,idx,replace):
        index=self.dic[idx]
        self.dic.pop(idx)
        self.dic[replace.key]=index
        self.heap[index]=replace
        self.down(index)
        self.up(index)
    def up(self,index):
        if index:
            parent=(index-1)//2
            if self.heap[index]>self.heap[parent]:
                self.dic[self.heap[parent].key]=index
                self.dic[self.heap[index].key]=parent
                self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
                self.up(parent)
    def down(self,index):
        tempindex=2*index+1
        if tempindex<self.size:
            right=2*index+2
            if right<self.size and self.heap[right]>self.heap[tempindex]:
                tempindex=right
            if self.heap[tempindex]>self.heap[index]:
                self.dic[self.heap[index].key]=tempindex
                self.dic[self.heap[tempindex].key]=index
                self.heap[tempindex],self.heap[index]=self.heap[index],self.heap[tempindex]
                self.down(tempindex)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        elif len(nums)<=k:
            return [max(nums)]
        Heap=MaxHeap()
        for i in range(k):
            Heap.add(Node(i,nums[i]))
        result=[Heap.getMax()]
        for i in range(k,len(nums)):
            Heap.replaceNode(i-k,Node(i,nums[i]))
            result.append(Heap.getMax())
        return result