class Solution:
    def minOperations(self, n: int) -> int:

        cnt=0
        
        while n>0:

            if n%2==0:

                n=n//2

            else:

                if n==1 or n&2==0:

                    n=n-1

                else:

                    n=n+1

                cnt=cnt+1


        return cnt

            