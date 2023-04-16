class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        
        res=[0]*len(grid[0])
        
        for i in range(len(grid[0])):
            
            for j in range(len(grid)):
                    
                res[i]=max(len(str(grid[j][i])),res[i])
                
        return res