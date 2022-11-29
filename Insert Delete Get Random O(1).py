import random
class RandomizedSet:

    def __init__(self):
        s1=set()
        self.s1=s1
        

    def insert(self, val: int) -> bool:
        if val not in self.s1:
            self.s1.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.s1:
            self.s1.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        self.s1=list(self.s1)
        val=random.randint(0, len(self.s1) - 1)
        a=self.s1[val]
        self.s1=set(self.s1)
        #print(self.s1)
        return a
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()