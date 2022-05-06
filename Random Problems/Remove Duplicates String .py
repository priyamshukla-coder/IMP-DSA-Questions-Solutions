'''

Problem Link :https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
T.C. : O(N)
S.C. : O(N)

'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        st=[]
        for i in s:
            if len(st)>0 and st[-1][0]==i:
                st[-1][1]=st[-1][1]+1
                if st[-1][1]==k:
                    st.pop()
            else:
                st.append([i,1])
            
        res=""
        for i in st:
            sr,c=i[0],i[1]
            res=res+(sr*c)
        
        return res