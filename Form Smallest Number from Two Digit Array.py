class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1,nums2=set(nums1),set(nums2)
        
        res=nums1.intersection(nums2)
        
        if len(res)>0:
            
            return min(res)
        
        return min(int(str(min(nums1))+str(min(nums2))),int(str(min(nums2))+str(min(nums1))))