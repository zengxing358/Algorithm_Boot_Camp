class Node:
    def __init__(self,value,key,pre=None,next=None):
        self.val=value
        self.key=key
        self.pre=pre
        self.next=next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=Node(47,"head")
        self.tail=Node(47,"tail")
        self.head.next=self.tail
        self.tail.pre=self.head
        self.map={}

    def get(self, key: int) -> int:
        if key in self.map:
            value=self.map[key].val
            self.__remove(key)
            self.__put(key,value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.__remove(key)
        elif len(self.map)==self.capacity:
            self.__pop()
        self.__put(key,value)

    def __put(self,key,value):
        newnode=Node(value,key,self.tail.pre,self.tail)
        self.tail.pre.next=newnode
        self.tail.pre=newnode
        self.map[key]=newnode

    def __pop(self):
        node=self.head.next
        self.map.pop(node.key)
        node.next.pre=self.head
        self.head.next=node.next

    def __remove(self,key):
        node=self.map[key]
        self.map.pop(key)
        node.pre.next=node.next
        node.next.pre=node.pre







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)