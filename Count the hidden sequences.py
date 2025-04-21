class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        cur = 0

        m1 , m2 =0 ,0

        for i in differences:

            cur += i

            m1 , m2 = min(m1 , cur) , max(m2 , cur)

        return max(0 , upper - m2 - lower + m1 + 1)
