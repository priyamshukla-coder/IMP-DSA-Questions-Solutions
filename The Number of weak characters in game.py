class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key=lambda x : (-x[0],x[1]))
        
        cnt=0
        curr_max=int(-1e9+7)
        print(properties)
        
        for i in properties:
            if i[1]<curr_max:
                cnt=cnt+1
            curr_max=max(curr_max,i[1])
        return cnt