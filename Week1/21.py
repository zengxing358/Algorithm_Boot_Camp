# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=ListNode(9)
        cur=res
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=ListNode(l1.val)
                l1=l1.next
            elif l1.val==l2.val:
                cur.next=ListNode(l1.val)
                cur=cur.next
                cur.next=ListNode(l2.val)
                l1=l1.next
                l2=l2.next
            else:
                cur.next=ListNode(l2.val)
                l2=l2.next
            cur=cur.next
        if l1:
            cur.next=l1
        if l2:
            cur.next=l2
        return res.next