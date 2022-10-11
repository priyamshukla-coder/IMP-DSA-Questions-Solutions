# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def length(node):
            
            l=0
            
            while node:
                l=l+1
                node=node.next
                
            return l
        
        l=length(head)
        
        st=0
        
        while st<l//2:
            
            head=head.next
            st=st+1
        
        return head