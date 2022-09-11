class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        d1={}
        
        for i in nums:
            if i%2==0:
                if i not in d1:
                    d1[i]=1
                else:
                    d1[i]=d1[i]+1
                    
        if len(d1)==0:
            return -1
        
        m=max(d1.values())
        res=[]
        
        for i in d1:
            if d1[i]==m:
                res.append(i)
        
        
        return sorted(res)[0]