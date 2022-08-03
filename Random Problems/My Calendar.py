class MyCalendar:

    def __init__(self):
        
        self.res=[]
        

    def book(self, start: int, end: int) -> bool:
        
        for i in self.res:
            
            st,ed=i[0],i[1]
            
            if st<end and start<ed:
                
                return False
            
        self.res.append([start,end])
        
        return True

# Time Complexity : O(n^2)
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)