'''
Problem Link : https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

'''

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        cnt=Counter(tasks)

        for i in cnt:

            if cnt[i]<=1:

                return -1


        min_time=0

        for i in cnt:

            min_time=min_time+ (cnt[i]//3 if cnt[i]%3==0 else cnt[i]//3+1)

        return min_time