# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build_tree(inorder,postorder):

            if not postorder or not inorder:

                return None

            node=TreeNode(postorder.pop())

            index=inorder.index(node.val)

            # node.left=build_tree(inorder[:index],postorder)

            node.right=build_tree(inorder[index+1:],postorder)

            node.left=build_tree(inorder[:index],postorder)

            return node

        return build_tree(inorder,postorder)