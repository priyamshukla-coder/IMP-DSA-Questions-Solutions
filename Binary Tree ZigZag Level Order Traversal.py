# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def traverse(root):

            flag,res=True,[]

            if root is None:

                return res

            q1=deque([])

            q1.append(root)

            while len(q1)>0:

                l=len(q1)

                curr=deque()

                for i in range(l):

                    node=q1.popleft()

                    if flag:

                        curr.append(node.val)

                    else:

                        curr.appendleft(node.val)

                    if node.left:

                        q1.append(node.left)

                    if node.right:

                        q1.append(node.right)

                res.append(curr)

                flag=not flag

            return res

        return traverse(root)