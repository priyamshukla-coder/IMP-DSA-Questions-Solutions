class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        
        def lst_index(s,char,curr_idx):
            
            s=s[::-1]
            
            st=0
            
            while s[st]!=char and st<len(s):
                
                st=st+1
                
            return len(s)-st-1
        
        if len(s) == len(set(s)):
            
            return -1
        
        mx=0
        
        seen=set()
        
        for i in range(len(s)):
            
            # print(s[i])
            
            if s[i] not in seen and s.count(s[i])>1:
                
                # print(s[i],lst_index(s,s[i],i))
                
                mx=max(mx,lst_index(s,s[i],i)-i-1)
            
                seen.add(s[i])
                
                # print(mx)
            
            
        return mx
            
                
            
                