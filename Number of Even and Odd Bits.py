class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res=bin(n)[2:][::-1]
        
        print(res)
        
        result=[0]*2
        
        for i in range(len(res)):
            
            if i%2 and res[i]=='1':
                
                result[1]+=1
                
            elif i%2==0 and res[i]=='1':
                
                result[0]+=1
                
        return result