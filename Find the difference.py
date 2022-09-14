class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        c=Counter(s)
        
        d=Counter(t)
        
        for i in d:
            
            if d[i]!=c[i] or i not in c:
                
                return i