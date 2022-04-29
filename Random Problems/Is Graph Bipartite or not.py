'''

Problem Link :https://leetcode.com/problems/is-graph-bipartite/
T.C. : O(V+E) E: No. of edges , V: No. of vertices
S.C. : O(V+E)

'''

from collections import deque,defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color=defaultdict(list)
        
        for i in range(len(graph)):
            if i not in color:
                color[i]=1
            q1=deque([])
            q1.append(i)
            while len(q1)>0:
                node=q1.popleft()
                for adj in graph[node]:
                    if adj not in color:
                        color[adj]= -color[node]
                        q1.append(adj)
                    elif color[adj]==color[node]:
                        return False
        return True