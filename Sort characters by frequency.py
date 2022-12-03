class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d1={}
        for i in s:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]=d1[i]+1
        d2= sorted(d1.items(), key = lambda s2:[s2[1], s2[0]],reverse=True)
        ##print(d2)
        s1=""
        for i in d2:
            a=i[0]
            b=i[1]
            s1=s1+(a*b)
        return s1