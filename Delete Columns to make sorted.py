class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        l=len(strs[0])

        cnt=0

        res=[[' ']*l]*len(strs)

        for i in range(len(strs)):

            for j in range(l):

                res[i][j]=res[i][j]+strs[i][j]

        curr=res[0]

        for i in curr:

            if "".join(sorted(i))!=i:

                cnt=cnt+1

        return cnt

