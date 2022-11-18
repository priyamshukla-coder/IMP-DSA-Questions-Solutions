class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        for i in range(2,6):
            while n%i==0:
                n=n//i
        if n==1:
            return True
        else:
            return False