from collections import defaultdict
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def check(s1,s2,l1,l2):
            if len(s1)!=len(s2):
                return False
            if s1==s2:
                return True
            if len(s1)==0:
                return False
            if sorted(s1)!=sorted(s2):
                return False
            if l2[(s1,s2)]:
                return l1[(s1,s2)]
            for i in range(1,len(s1)):
                if (check(s1[i:],s2[i:],l1,l2) and check(s1[:i],s2[:i],l1,l2)) or (check(s1[-i:],s2[:i],l1,l2) and check(s1[:-i],s2[i:],l1,l2)):
                    l1[(s1,s2)]=True
                    break
            l2[(s1,s2)]=True
            return l1[s1,s2]
        l1=defaultdict(lambda:False)
        l2=defaultdict(lambda:False)
        return check(s1,s2,l1,l2)
    