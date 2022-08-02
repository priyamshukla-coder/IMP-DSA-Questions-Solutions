class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def recur(st,end,grid): #TLE 
            
            if st==0 and end==0:
                return grid[0][0]
            
            if st<0 or end<0:
                return float("inf")
            
            up=grid[st][end]+recur(st-1,end,grid)
            left=grid[st][end]+recur(st,end-1,grid)
            
            return min(up,left)
        
        # return recur(len(grid)-1,len(grid[0])-1,grid)
        
        #Time complexity : 2^(m*n) (as every index has 2 options up or left if we start from last end of matrix)
        #Space complexity : Path Length = (m-1)+(n-1)
        
        def optimize(st,end,grid,dp):
            
            # dp=[[-1 for _ in range(end+1)] for _ in range(st+1)]
            
            if st==0 and end==0:
                return grid[0][0]
            
            if st<0 or end<0:
                return int(1e7)
            
            if dp[st][end]!=-1:
                return dp[st][end]
            
            up=grid[st][end]+optimize(st-1,end,grid,dp)
            left=grid[st][end]+optimize(st,end-1,grid,dp)
            
            dp[st][end]=min(up,left)
            
            return dp[st][end]
        
        dp=[[-1 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        # print(dp)
        
        # return optimize(len(grid)-1,len(grid[0])-1,grid,dp)
        
        #Time complexity : O(m*n)
        #S.C. : O((m-1)+(n-1))  + O(m*n)
        
        def tabulate(st,end,grid):
            
            dp=[[0 for _ in range(end+1)] for _ in range(st+1)]
            
            dp[0][0]=grid[0][0]
            
            for i in range(0,st):
                
                for j in range(0,end):
                    
                    if i==0 and j==0:
                        dp[i][j]=grid[i][j]
                        
                    else:
                        up=grid[i][j]
                        if i>0:
                            up=up+dp[i-1][j]
                        else:
                            up=up+int(1e7)
                            
                        left=grid[i][j]
                        if j>0:
                            left=left+dp[i][j-1]
                        else:
                            left=left+int(1e7)
                    
                        dp[i][j]=min(up,left)
                        # print(dp)
                
            return dp[st-1][end-1]
        
            #Time complexity : O(m*n)
            #S.C. : O((m-1)+(n-1))  + O(m*n)
            
        return tabulate(len(grid),len(grid[0]),grid)