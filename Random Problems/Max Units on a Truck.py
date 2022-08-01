<<<<<<< HEAD
'''
Problem Link : https://leetcode.com/problems/maximum-units-on-a-truck/

'''

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        print(boxTypes)
        ans=0
        for i in boxTypes:
            a,b=i[0],i[1]
            if truckSize>a:
                truckSize=truckSize-a
                ans=ans+(a*b)
            else:
                ans=ans+(truckSize*b)
                return ans
=======
'''
Problem Link : https://leetcode.com/problems/maximum-units-on-a-truck/

'''

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        print(boxTypes)
        ans=0
        for i in boxTypes:
            a,b=i[0],i[1]
            if truckSize>a:
                truckSize=truckSize-a
                ans=ans+(a*b)
            else:
                ans=ans+(truckSize*b)
                return ans
>>>>>>> 85d33560c6ab825edd64dd3148fd495f90d50bd3
        return ans