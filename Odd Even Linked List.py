# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        o,e=head,head.next
        e_head=e
        while e!=None and e.next !=None:
            o.next=e.next
            o=o.next
            e.next=o.next
            e=e.next
        o.next=e_head
        return head