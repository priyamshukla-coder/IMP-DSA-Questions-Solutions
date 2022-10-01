class LUPrefix:
    

    def __init__(self, n: int):
        
        a=[0]*n
        
        self.st=0
        
        self.a=[0]*n
        
#         for st in range(n):
            
#             self.a[st]=0
        
        

    def upload(self, video: int) -> None:
        
        self.a[video-1]=1
        
        while self.st<len(self.a):

            if self.a[self.st]==0:

                break

            self.st=self.st+1
        

    def longest(self) -> int:
        
#         global st
        
#         while st<len(self.a):
            
#             if self.a[st]==0:
                
#                 break
                
#             st=st+1
            
        return self.st


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()