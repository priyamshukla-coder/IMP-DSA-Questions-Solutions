class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def can_split_array(nums,mid,k):

            ways=1

            curr_sum=0

            for i in range(len(nums)):

                curr_sum=curr_sum+nums[i]

                if curr_sum>mid:

                    ways=ways+1

                    curr_sum=nums[i]

            return True if ways<=k else False

        if len(nums)==k:

            return max(nums)

        low,high,res=max(nums),sum(nums),0

        while low<=high:

            mid=low+(high-low)//2

            if can_split_array(nums,mid,k):

                res=mid

                high=mid-1

            else:

                low=mid+1

        return res