class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        res=[]
        
        for i in range(len(names)):
            
            res.append([heights[i],names[i]])
            
        res.sort(reverse=True)
        
        ans=[]
        
        for i in res:
            
            ans.append(i[1])
            
        return ans