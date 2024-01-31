class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # T.C. : O(V+E)
        # S.C. : O(V)

        def dfs(node,vis,graph):

            vis[node]=True

            for neigh in graph[node]:

                if vis[neigh] != True:

                    dfs(neigh,vis,graph)

        vis=[False]*len(rooms)

        # for i in range(0,len(rooms)):

            # if vis[i] != True:

        dfs(0,vis,rooms) # we are at room 0 so we start dfs from 0 and it will keep on going.

        print(vis)

        for i in vis:

            if i==False:

                return False

        return True
