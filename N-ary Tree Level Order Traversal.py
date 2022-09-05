"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        def bfs(root):
        
            if root == None:
                return []

            res=[]
            q1=deque([])
            q1.append(root)

            while len(q1)>0:

                n=len(q1)
                curr=[]

                # node=q1.popleft()
                # curr.append(node.val)

                for i in range(n):
                    
                    node=q1.popleft()
                    curr.append(node.val)
                    # print(curr)

                    if node.children is not None:
                        
                        for vl in node.children:

                            q1.append(vl)

                res.append(curr)
            
            return res
            
        return bfs(root)