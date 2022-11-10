class Solution:
    def removeDuplicates(self, s: str) -> str:

        s=list(s)

        st=[]

        for i in range(len(s)):

            if len(st)>0 and st[-1]==s[i]:

                st.pop()

            else:

                st.append(s[i])

        return "".join(st)