class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        cnt=0
        res=[]
        
        for i in range(len(nums)-2):
            
            st=i+1
            end=len(nums)-1
            
            while st<end:
                if nums[st]+nums[end]+nums[i]==0 and [nums[i],nums[st],nums[end]] not in res:
                    res.append([nums[i],nums[st],nums[end]])
                elif nums[st]+nums[end]+nums[i]>0:
                    end=end-1
                else:
                    st=st+1
                
        return res