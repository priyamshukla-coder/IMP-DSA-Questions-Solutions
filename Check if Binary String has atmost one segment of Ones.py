class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
#         cnt=0
        
#         mx=0
        
#         for i in s:
            
#             if i=='1':
                
#                 cnt=cnt+1
                
#                 mx=max(mx,cnt)
                
#             else:
                
#                 cnt=0
                
#         return True if mx>=2  or len(s)==1 and mx==1 else False

        
        for i in range(len(s)-1):
            
            if s[i]=='0' and s[i+1]=='1':
                
                return False
            
        return True