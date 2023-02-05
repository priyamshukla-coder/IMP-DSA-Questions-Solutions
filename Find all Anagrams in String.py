from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        c,d={i:0 for i in range(97,123)},{i:0 for i in range(97,123)}
        
        res=[]
        
        if len(s)<len(p):
            
            return res
        
        for i in range(0,len(p)):
            
            c[ord(s[i])]=c[ord(s[i])]+1
            
            d[ord(p[i])]=d[ord(p[i])]+1
            
        if c==d:
            
            res.append(0)
            
        st=len(p)-1
        
        for i in range(len(p),len(s)):
            
            c[ord(s[i-len(p)])]-=1
            
            c[ord(s[i])]+=1
            
            if c==d:
                
                res.append(i-len(p)+1)
            
        return res