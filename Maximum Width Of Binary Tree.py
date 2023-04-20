# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q1=deque([(root,0)])

        max_width=0

        while len(q1)>0:

            l=len(q1)

            curr=q1[0][1]

            for i in range(l):

                tree_node,curr_width=q1.popleft()

                if tree_node.left:

                    q1.append((tree_node.left,2*curr_width))

                if tree_node.right:

                    q1.append((tree_node.right,2*curr_width+1))

            max_width=max(max_width,-1*curr+curr_width+1)

        return max_width