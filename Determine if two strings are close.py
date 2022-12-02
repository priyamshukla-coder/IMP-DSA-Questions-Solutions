from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1,c2=Counter(word1),Counter(word2)
        if set(word1)==set(word2):
            if Counter(c1.values())==Counter(c2.values()):
                return True
            else:
                return False
        else:
            return False