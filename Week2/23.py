class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists:
            if len(lists)==1:
                return lists[0]
            else:
                mid=len(lists)//2
                left=self.mergeKLists(lists[:mid])
                right=self.mergeKLists(lists[mid:])
                head=ListNode(49)
                cur=head
                while left and right:
                    if left.val<right.val:
                        cur.next=ListNode(left.val)
                        left=left.next
                    else:
                        cur.next=ListNode(right.val)
                        right=right.next
                    cur=cur.next
                if left:
                    cur.next=left
                else:
                    cur.next=right
                return head.next