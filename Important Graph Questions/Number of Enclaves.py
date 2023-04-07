class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def dfs(i,j,grid):

            if i==-1 or j==-1 or i==len(grid) or j==len(grid[0]) or grid[i][j]==0:

                return 

            grid[i][j]=0

            dfs(i+1,j,grid)

            dfs(i-1,j,grid)

            dfs(i,j+1,grid)

            dfs(i,j-1,grid)

        for i in range(0,len(grid)):

            for j in range(0,len(grid[0])):

                if i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1:

                    if grid[i][j]==1:

                        dfs(i,j,grid)

        cnt=0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                cnt=cnt+grid[i][j]

        return cnt