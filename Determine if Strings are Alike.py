class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        s=s.lower()

        frnt,bck=s[:len(s)//2],s[len(s)//2:]

        vwl=['a','e','i','o','u']

        cnt1,cnt2=0,0

        for i in frnt:

            if i in vwl:

                cnt1=cnt1+1

        for i in bck:

            if i in vwl:

                cnt2=cnt2+1

        return True if cnt1==cnt2 else False