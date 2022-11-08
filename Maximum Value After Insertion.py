class Solution:
    def maxValue(self, n: str, x: int) -> str:

        if n[0]!='-':

            st=0

            while st<len(n) and str(x)<=n[st]:

                st=st+1

        else:

            st=1

            while st<len(n) and str(x)>=n[st]:

                st=st+1

        return n[:st]+str(x)+n[st:]