class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        s1,s2=set(nums1),set(nums2)
        
        s1=s1.intersection(s2)
        
        return sorted(list(s1))[0] if len(s1)>0 else -1