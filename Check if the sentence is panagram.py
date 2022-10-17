class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        d1={chr(i):0 for i in range(97,123)}
        
        for i in sentence:
            
            d1[i]=d1[i]+1
            
        for i in range(97,123):
            
            if d1[chr(i)]==0:
                
                return False
            
        return True