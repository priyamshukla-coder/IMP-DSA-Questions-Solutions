class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        st=[]

        index=0

        for i in pushed:

            st.append(i)

            while len(st)>0 and st[-1]==popped[index]:

                st.pop()

                index=index+1

        return True if index==len(popped) else False