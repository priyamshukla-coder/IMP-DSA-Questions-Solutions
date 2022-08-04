'''
Problem Link : https://leetcode.com/problems/design-hashset/

'''

class MyHashSet:

    def __init__(self):
        s1=set()
        self.s1=s1
        

    def add(self, key: int) -> None:
        self.s1.add(key)

    def remove(self, key: int) -> None:
        if key in self.s1:
            self.s1.remove(key)
            
    def contains(self, key: int) -> bool:
        if key in self.s1:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)