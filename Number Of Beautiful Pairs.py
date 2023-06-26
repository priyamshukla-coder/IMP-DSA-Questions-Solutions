class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        
        cnt=0
        
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):
                
                # print(gcd(nums[i],nums[j]))
                
                a,b=str(nums[i])[0],str(nums[j])[-1]
                
                if gcd(int(a),int(b))==1:
                
                    cnt=cnt+1
                
        return cnt