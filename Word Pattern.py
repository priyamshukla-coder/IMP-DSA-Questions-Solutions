class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        d1={}

        d2={}

        s=s.split(" ")

        if len(s) != len(pattern):

            return False

        j=0

        for i in range(len(pattern)):

            curr1,curr2=pattern[i],s[i]

            if curr1 not in d1:

                d1[curr1]=j

            if curr2  not in d2:

                d2[curr2]=j

            j=j+1

        for i in range(len(pattern)):

            if d1[pattern[i]]!=d2[s[i]]:

                return False

        return True