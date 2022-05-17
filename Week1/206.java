class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode last=null;
        while(head!=null){
           ListNode nextHead=head.next;
            head.next=last;
            last=head;
            head=nextHead;
        }
        return last;
    }
}