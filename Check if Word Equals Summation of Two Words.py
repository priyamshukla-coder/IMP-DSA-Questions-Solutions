class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        d1={chr(i):0 for i in range(97,123)}

        x,y,z,cnt="","","",0

        for i in range(97,123):

            d1[chr(i)]=cnt

            cnt=cnt+1

        for i in firstWord:
            
            x=x+str(d1[i])

        for i in secondWord:

            y=y+str(d1[i])

        for i in targetWord:

            z=z+str(d1[i])

        # print(x,y,z)

        return True if int(x)+int(y)==int(z) else False


