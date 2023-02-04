class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        def separate(n):
            
            res=[]
            
            while n>0:
                
                res.append(n%10)
                
                n=n//10
                
            return res[::-1]
        
        result=[]
        
        for i in nums:
            
            result=result+separate(i)
            
        return result