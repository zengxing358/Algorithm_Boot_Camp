class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast,slow=head,head
        while True:
            if not (fast and fast.next):
                return
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break
        slow=head
        while fast!=slow:
            fast,slow=fast.next,slow.next
        return fast