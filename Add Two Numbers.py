# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=ListNode(0)
        cur=s1
        carry=0
        while l1!=None or l2!=None:
            if l1 is not None:
                a=l1.val
            else:
                a=0
            if l2 is not None:
                b=l2.val
            else:
                b=0
            curr_sum=a+b+carry
            carry=curr_sum//10
            cur.next=ListNode(curr_sum%10)
            cur=cur.next
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        if carry>0:
            cur.next=ListNode(carry)
        return s1.next
