from collections import Counter
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d1=dict()
        ws=0
        we=0
        m1=0
        for we in range(1,len(s)+1):
            if s[we-1] in d1:
                ws=max(ws,d1[s[we-1]]+1)
            d1[s[we-1]]=we-1
            m1=max(m1,(we-1)-ws+1)
        return m1
        