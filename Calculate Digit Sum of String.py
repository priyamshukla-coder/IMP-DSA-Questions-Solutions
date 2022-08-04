'''
https://leetcode.com/problems/calculate-digit-sum-of-a-string/

'''

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            curr=[]
            for i in range(0,len(s),k):
                    curr.append(s[i:i+k])
            #print(curr)
            res=""
            for i in curr:
                res=res+str(sum(list(map(int,str(i)))))
            s=res
        return s