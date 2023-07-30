class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        cnt_emp=0
        
        for i in range(len(hours)):
            
            cnt_emp=cnt_emp+(hours[i]>=target)
            
        return cnt_emp