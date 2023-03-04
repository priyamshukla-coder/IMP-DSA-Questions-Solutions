class Solution:
    def splitNum(self, num: int) -> int:

        res=[]

        while num>0:

            res.append(num%10)

            num=num//10

        res.sort()

        n1,n2="",""

        res=list(map(str,res))

        for i in range(0,len(res),2):

            n1=n1+res[i]

        for j in range(1,len(res),2):

            n2=n2+res[j]

        return int(n1)+int(n2)