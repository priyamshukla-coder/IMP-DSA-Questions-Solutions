# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def length(node):
            
            l=0
            while node:
                l=l+1
                node=node.next
            
            return l
        
        l=length(head)
        
        st=0
        
        curr,prev=head,head
        
        
        if l==1:
            return ListNode(0).next
        
        if l==n:
            return curr.next
    
        
        s=None
        
        while st<(l-n):
            
            prev=curr
            curr=curr.next
            st=st+1
        
        prev.next=curr.next
        curr=None
        
        return head
            