class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        s=ListNode(7)
        last=s
        cur=head
        while cur:
            end=self.getend(cur,k)
            if not end:
                last.next=cur
                break
            nextcur=end.next
            self.reverse(cur,end)
            last.next=end
            last=cur
            cur=nextcur
        return s.next
    def getend(self,node,k):
        while node:
            k-=1
            if k==0:
                return node
            node=node.next
        return node
    def reverse(self,cur,end):
        t=None
        while cur!=end:
            nextc=cur.next
            cur.next=t
            t=cur
            cur=nextc
        cur.next=t