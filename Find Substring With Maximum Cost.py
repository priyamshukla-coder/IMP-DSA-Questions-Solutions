class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
#         Kadane's Algorithm Implementation 
        
        d1={chr(i+96):i  for i in range(1,27)}
        
        curr,curr_max=0,0
        
        for i in range(len(chars)):
            
            d1[chars[i]]=vals[i]
            
        for i in s:
            
            curr=max(0,curr+d1[i])
            
            curr_max=max(curr_max,curr)
            
        return curr_max