class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        mx1,mx2=float("inf"),float("inf")
        
        for i in nums:
            
            if i<=mx1:
                
                mx1=i
                
            elif i<=mx2:
                
                mx2=i
            
            else:
                
                return True
            
        return False