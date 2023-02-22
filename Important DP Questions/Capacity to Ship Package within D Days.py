class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_load_all_weights(weights,mid,days):
            
            curr_used_days=1

            curr_weight=0

            for i in range(len(weights)):

                curr_weight=curr_weight+weights[i]

                if curr_weight>mid:

                    curr_used_days=curr_used_days+1

                    curr_weight=weights[i]

            return True if curr_used_days<=days else False

        if len(weights)==days:

            return max(weights)

        low,high=max(weights),sum(weights)

        while low<=high:

            mid=low+(high-low)//2

            if can_load_all_weights(weights,mid,days):

                res=mid

                high=mid-1

            else:

                low=mid+1

        return res