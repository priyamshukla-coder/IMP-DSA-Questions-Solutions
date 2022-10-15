from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(x,y,inc,nc,image):
            if x<0 or y<0:
                return 
            if x >= len(image)  or y >= len(image[0]):
                return 
            if image[x][y] != inc:
                return 
            image[x][y] = nc
            dfs(x+1,y,inc,nc,image)
            dfs(x-1,y,inc,nc,image)
            dfs(x,y+1,inc,nc,image)
            dfs(x,y-1,inc,nc,image)
        inc=image[sr][sc]
        if inc!=newColor:
            dfs(sr,sc,inc,newColor,image)
        return image