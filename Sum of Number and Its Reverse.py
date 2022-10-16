class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        
        def compute(n):
            
            for i in range(n//2,n+1):
                
                if int(str(i))+int(str(i)[::-1])==n:
                    
                    return True
                
            return False
        
        return compute(num)