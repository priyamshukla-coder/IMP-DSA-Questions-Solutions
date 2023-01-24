class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        if k==0 and nums1==nums2:
            
            return 0
        
        elif k==0 and nums1!=nums2:
            
            return -1
    
        pos,neg=0,0
        
        for i in range(len(nums1)):
            
            if nums1[i]>=nums2[i]:
                
                if (nums1[i]-nums2[i])%k==0:
                
                    pos=pos+(nums1[i]-nums2[i])
                    
                else:
                    
                    return -1
                
            else:
                
                if (-nums1[i]+nums2[i])%k==0:
                    
                    neg=neg+(nums2[i]-nums1[i])
                    
                else:
                    
                    return -1
                
        print(pos,neg)
                
            
        return -1 if pos!=neg else pos//k
                
                