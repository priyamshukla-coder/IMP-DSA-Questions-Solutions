<<<<<<< HEAD
'''
Problem Link : https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

'''

from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        
        freq=Counter(s)
        
        #print(freq)
        
        cnt=0
        
        s1=[]
        
        for i in freq:
            
            if freq[i] in s1:
                
                while freq[i]>0 and freq[i] in s1:
                    
                        freq[i]=freq[i]-1
                        
                        cnt=cnt+1
                        #print(freq[i])
                        
            s1.append(freq[i])
            
            #print(s1)
            
=======
'''
Problem Link : https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

'''

from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        
        freq=Counter(s)
        
        #print(freq)
        
        cnt=0
        
        s1=[]
        
        for i in freq:
            
            if freq[i] in s1:
                
                while freq[i]>0 and freq[i] in s1:
                    
                        freq[i]=freq[i]-1
                        
                        cnt=cnt+1
                        #print(freq[i])
                        
            s1.append(freq[i])
            
            #print(s1)
            
>>>>>>> 85d33560c6ab825edd64dd3148fd495f90d50bd3
        return cnt