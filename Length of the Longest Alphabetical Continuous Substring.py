class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        mx=1
        
        cur=1
        
        char=s[0]
        
        for i in s[1:]:
            
            if ord(char)+1==ord(i):
                
                # print(ord(char),ord(i))
                
                cur=cur+1
                
                mx=max(cur,mx)
                
                
            else:
                
                cur=1
                
            char=i
                
            # print(cur,mx)
                
        return mx