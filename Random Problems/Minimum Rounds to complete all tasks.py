'''
Problem Link : https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

'''

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        c=Counter(tasks)
        
        for i in c:
            if c[i]<2:
                return -1
    
        min_time=0
        
        for i in c:
            min_time=min_time+((c[i]//3) if c[i]%3==0 else c[i]//3+1)
            #print(min_time)
        return min_time