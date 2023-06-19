class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        prefix=[0]*(len(gain)+1)

        # prefix[0]=gain[0]

        i,j=1,0

        while i<len(gain) and j<len(gain):

            prefix[i]=prefix[i-1]+gain[j]

            i=i+1

            j=j+1

        prefix[-1]=prefix[-2]+gain[-1]

        return max(max(prefix),0)