class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        
        def cal(mat,cols,res,st):
            
            nonlocal cnt
            
            if cols==0:
                
                c=0
                
                for i in range(len(mat)):
                    
                    status=False
                    
                    for j in range(0,len(mat[i])):
                        
                        if mat[i][j]==1 and res[j]==0:
                            
                            #if res[j]==0:
                                
                            status=True

                            break
                                
                    if status==False:
                        
                        c=c+1
                        
                cnt=max(cnt,c)
                # print(cnt)
                
                return 
                 
            
            for i in range(st,len(mat[0])):
                
                res[i]=1
                
                cal(mat,cols-1,res,i+1)
                
                res[i]=0
            
            # return cnt
                
        # global cnt
        
        cnt=0
        
        res=[0]*len(mat[0])
        
        cal(mat,cols,res,0)
        
        return cnt