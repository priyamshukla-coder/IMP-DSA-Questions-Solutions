class Solution:
    def reverseWords(self, s: str) -> str:
        
        res=""
        s1=' '
        s=s+" "
        
        for i in range(len(s)):
            
            if s[i]!=' ':
            
                curr=s[i]

                s1=curr+s1
                
                print(s1)
                
            elif s[i]==' ':
                
                res=res+s1
                
                s1=' '
                
        
        # print(res+s1)
        
        return res[:len(res)-1]