class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # d1={i:0 for i in range(1,100000+1)}
        # d2={i:0 for i in range(1,100000+1)}

        d1=defaultdict(lambda : [0,0])

        for i in matches:

            win,loss=i[0],i[1]

            d1[win][0]=d1[win][0]+1

            d1[loss][1]=d1[loss][1]+1

        win,loss,res=[],[],[[],[]]
        for i in d1:

            if d1[i][1]==0:

                res[0].append(i)

            elif d1[i][1]==1:

                res[1].append(i)

        res[0].sort()

        res[1].sort()

        # res.append(win)

        # res.append(loss)

        return res
        
                   