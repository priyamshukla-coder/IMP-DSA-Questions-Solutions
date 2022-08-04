import bisect
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        st=matrix[0][0]
        end=matrix[len(matrix)-1][len(matrix)-1]
        # cnt=0
        
        while st<end:
            
            cnt=0
            
            mid=(st+(end-st)//2)
            
            for i in range(len(matrix)):
                
                val=bisect_right(matrix[i],mid)
                
                cnt=cnt+val
                
            if cnt<k:
                
                st=mid+1
            
            else:
                
                end=mid
                
        return st