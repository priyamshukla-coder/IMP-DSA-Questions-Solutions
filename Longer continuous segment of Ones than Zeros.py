class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        mx_one=0
        
        mx_zero=0
        
        cnt_one=0
        
        cnt_zero=0
        
        for i in s:
            
            if i=='1':
                
                cnt_one=cnt_one+1
                
                mx_one=max(mx_one,cnt_one)
                
                cnt_zero=0
                
            elif i=='0':
                
                cnt_zero=cnt_zero+1
                
                mx_zero=max(mx_zero,cnt_zero)
                
                cnt_one=0
        
            # print(mx_zero,mx_one)
        
        return True if mx_one>mx_zero else False