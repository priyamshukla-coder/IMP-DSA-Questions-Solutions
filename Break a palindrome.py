class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        c=Counter(palindrome)
        palin=list(palindrome)
        for i in range(len(palin)//2):
            if palin[i]!='a':
                palin[i]='a'
                return "".join(palin)
        palin[len(palin)-1]='b'
        return "".join(palin)