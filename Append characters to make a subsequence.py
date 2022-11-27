class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i,j=0,0
        
        while i<len(s) and j<len(t):
            
            if s[i]==t[j]:
                
                j=j+1
                
            i=i+1
            
            
        return len(t)-j