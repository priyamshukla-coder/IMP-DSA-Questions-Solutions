# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def length(s1):
            
            i=0
            
            while s1:
                
                i=i+1
                
                s1=s1.next
                
            return i
        
        l=length(head)
        
        if l==1:
            
            return ListNode(0).next

        curr,prev=head,head

        st=0

        while st<l//2:

            prev=curr

            curr=curr.next

            st=st+1

        prev.next=curr.next

        curr=prev

        return head
            
            