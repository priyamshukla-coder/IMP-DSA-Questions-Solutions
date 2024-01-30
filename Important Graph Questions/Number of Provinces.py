class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # S.C. : O(N) // for visited array
        # T.C. : O(N)+O(V+2*E) ~~O(N)

        def dfs(node,graph,vis):

            vis[node]=1

            for neighbour in graph[node]:

                if vis[neighbour]!=1:

                    dfs(neighbour,graph,vis)

        adj_mat=defaultdict(list)

        n=len(isConnected)

        for i in range(n):

            for j in range(n):

                if i!=j and isConnected[i][j]==1:

                    adj_mat[i].append(j)

                    adj_mat[j].append(i)

        cnt=0

        visited=[0]*n

        for i in range(n):

            if visited[i]!=1:

                cnt=cnt+1

                dfs(i,adj_mat,visited)

        return cnt        