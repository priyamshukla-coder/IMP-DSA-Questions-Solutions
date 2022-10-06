import bisect
class TimeMap:

    def __init__(self):
        
        self.d1={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.d1:
            
            self.d1[key]=[]
            
        self.d1[key].append([timestamp,value])
        
        # print(self.d1)
        

    def get(self, key: str, timestamp: int) -> str:
        
        # keys=sorted(self.d1)
        
        # print(keys)
    
        
        if key not in self.d1:
            
            return ""
        
        ind = bisect.bisect(self.d1[key], timestamp,key=itemgetter(0))
        
        # print(ind)
        
        return "" if ind<=0 else self.d1[key][ind-1][1]
    
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)