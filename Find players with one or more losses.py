class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d1={i:0 for i in range(1,100000+1)}
        d2={i:0 for i in range(1,100000+1)}
        for i in matches:
            a,b=i[0],i[1]
            if a in d1:
                d1[a]=d1[a]+1
            else:
                d1[a]=1
            if b not in d2:
                d2[b]=1
            else:
                d2[b]=d2[b]+1
        
        w,loss,res=[],[],[]
        for i in range(1,100000+1):
            if d1[i]>=1 and d2[i]==0:
                w.append(i)
            else:
                if d2[i]==1:
                    loss.append(i)
        res.append(w)
        res.append(loss)

        return res
        
                   