class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowel=['A','E','I','O','U','a','e','i','o','u']
        
        pos=[]
        
        map=[]
        
        for i in range(len(s)):
            
            if s[i] in vowel:
                
                pos.append(i)
                
                map.append(s[i])
                
        map.sort()
        
        s=list(s)
        
        ans=s
        
        for i in range(len(pos)):
            
            ans[pos[i]]=map[i]
            
        return "".join(ans)   