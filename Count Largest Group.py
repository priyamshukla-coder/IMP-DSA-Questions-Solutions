class Solution:
    def countLargestGroup(self, n: int) -> int:
        l1=[0]*(36+1)
        for i in range(1,n+1):
            s1=sum(list(map(int,str(i))))
            #print(s1)
            l1[s1]=l1[s1]+1
        return l1.count(max(l1))
            
