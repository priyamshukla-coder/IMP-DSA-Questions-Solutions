class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def area(x1, y1, x2, y2):
            return (x2 - x1) * (y2 - y1)
        
        def overlap(a2, b2, a1, b1):
            return max(min(a2, b2) - max(a1, b1), 0)
        
        return area(ax1, ay1, ax2, ay2) + area(bx1, by1, bx2, by2) - overlap(ax2, bx2, ax1, bx1) * overlap(ay2, by2, ay1, by1)