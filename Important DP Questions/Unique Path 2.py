class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def recur(st,end,matrix):
            
            if st>=0 and end>=0 and matrix[st][end]==1:
                return 0
            
            if st==0 and end==0:
                return 1
            #reached start of the grid 
            
            if st<0 or end<0:
                return 0
            #when exceed the boundaries of left and down 
            
            
            #if we start from bottom we can move upwards or left
            #upwards -> row -1 ,col=same
            #left -> row=same,col-1
            
            up=recur(st-1,end,matrix)
            
            left=recur(st,end-1,matrix)
            
            return up+left
        
        # return recur(len(obstacleGrid)-1,len(obstacleGrid[0])-1,obstacleGrid)
        
        #Time complexity : 2^(m*n) (as every index has 2 options up or left if we start from last end of matrix)
        #Space complexity : Path Length = (m-1)+(n-1)
        
        def memoize(st,end,matrix,dp):
            # dp=[[-1 for _ in range(end+1)] for _ in range(st+1)]
            
            if st>=0 and end>=0 and matrix[st][end]==1:
                return 0
            
            if st==0 and end==0:
                return 1
            
            
            if st<0 or end <0:
                return 0
            
            if dp[st][end]!=-1:
                return dp[st][end]
            
            
            up=memoize(st-1,end,matrix,dp)
            
            left=memoize(st,end-1,matrix,dp)
            
            dp[st][end]=up+left
            
            return dp[st][end]
            
        # dp=[[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        
        # return memoize(len(obstacleGrid)-1,len(obstacleGrid[0])-1,obstacleGrid,dp)
            
        #Time complexity : O(m*n)
        #S.C. : O((m-1)+(n-1))  + O(m*n)
        
        def tabulation(st,end,dp,matrix):
            
            # dp=[[1 for _ in range(end+1)] for _ in range(st+1)]
            
            # dp[0][0]=1
            
            for i in range(st):
                
                for j in range(end):
                    
                    if matrix[i][j]==1:
                        dp[i][j]=0
                    
                    elif i==0 and j==0:
                        dp[i][j]=1
                        
                    else:
                        
                        up,left=0,0
                        
                        if i>0:
                            up=dp[i-1][j]
                        
                        if j>0:
                            left=dp[i][j-1]
                            
                        dp[i][j]=up+left
                    
            #print(dp)
                    
            return dp[st-1][end-1]
        
            #S.C.=O(M*N)
            #T.C.=O(M*N)
        
        dp=[[1 for _ in range(len(obstacleGrid[0])+1)] for _ in range(len(obstacleGrid)+1)]
        return tabulation(len(obstacleGrid),len(obstacleGrid[0]),dp,obstacleGrid)