# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def traversal(root):

            res=deque()

            while root:

                res.append(root.val)

                root=root.next

            return res

        def make_bst(res,st,end):

            if st>end:

                return None

            mid=st+(end-st)//2

            tree=TreeNode(res[mid])

            tree.left=make_bst(res,st,mid-1)

            tree.right=make_bst(res,mid+1,end)

            return tree

        res=traversal(head)

        # print(res)

        return make_bst(res,0,len(res)-1)

            

            