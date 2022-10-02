class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        def fact(n):
            
            res=[]
            
            for i in range(1,n+1):
                
                if n%i==0:
                    
                    res.append(i)
                    
            return res
        
        c,d=fact(a),fact(b)
        
        c,d=set(c),set(d)
        
        return len(c.intersection(d))