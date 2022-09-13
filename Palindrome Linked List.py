# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def rev_list(head):
            
            s1,s2=None,None
            
            while head!=None:
                
                s2=head.next
                
                head.next=s1
                
                s1=head
                
                head=s2
                
            return s1
        
        if head==None or head.next==None:
            
            return True
            
        slow=head
        
        fast=head 
        
        while fast.next!=None and fast.next.next!=None:
            
            slow=slow.next
            
            fast=fast.next.next
            
        slow.next=rev_list(slow.next)
        
        slow=slow.next
        
        while slow!=None:
            
            if slow.val!=head.val:
                
                return False
            
            slow=slow.next
            
            head=head.next
            
        return True