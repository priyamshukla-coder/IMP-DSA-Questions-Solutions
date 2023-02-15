class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        res=""

        for i in num:

            res=res+str(i)

        curr=int(res)+k

        return list(map(int,str(curr)))