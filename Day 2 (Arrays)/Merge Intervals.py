'''
Problem Link : https://leetcode.com/problems/merge-intervals/
T.C. : O(NlogN)+O(N)
S.C. : O(N)

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort()
        #print(intervals)
        prev_interval=intervals[0]
        l1=[]
        for i in range(1,n):
            if intervals[i][0]<=prev_interval[1]:
                prev_interval[1]=max(prev_interval[1],intervals[i][1])
            else:
                l1.append(prev_interval)
                #print(l1)
                prev_interval=intervals[i]
        l1.append(prev_interval)
        return l1