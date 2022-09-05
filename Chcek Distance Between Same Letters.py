class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
        def second_occur(s,curr_idx,char):
            
            idx=curr_idx+1
            
            while s[idx]!=char:
                
                idx=idx+1
                
            return idx
            
        
        status=True
        
        visited=[]
        
        for i in range(len(s)):
            
            if s[i] not in visited:
                
                st_idx=i
                
                lst_idx=second_occur(s,i,s[i])
                
                # print(st_idx,lst_idx)
                
                # print(lst_idx-st_idx-1)
                
                if distance[ord(s[i])-97]==lst_idx-st_idx-1:
                    
                    status=True
                    
                else:
                    
                    return False
                
                visited.append(s[i])
        
        return True
            
        
                
            