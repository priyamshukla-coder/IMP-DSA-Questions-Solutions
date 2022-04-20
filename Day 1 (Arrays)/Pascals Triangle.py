'''
Problem Link : https://leetcode.com/problems/pascals-triangle/
Date : 14/04/2022

'''

import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l1=[]
        for i in range(numRows):
            l1.append([])
            for j in range(i+1):
                if j==0 or j==i:
                    l1[i].append(1)
                else:
                    l1[i].append(l1[i-1][j-1]+l1[i-1][j])
        return l1
                
                