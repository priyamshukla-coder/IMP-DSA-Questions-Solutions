class Solution:
    def maximum69Number (self, num: int) -> int:

        l=list(str(num))

        if l.count('9')==len(l):

            return int("".join(l))

        for i in range(len(l)):

            if l[i]=='6':

                l[i]='9'

                break

        return int("".join(l))

                