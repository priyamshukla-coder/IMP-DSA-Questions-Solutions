class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        #T.C. : O(m*n)
        #S.C. : O(m*n)

        def dfs(sr,sc,image,ans,color,deltaRow,deltaCol,iniCol):

            image[sr][sc] = color

            m , n = len(image) , len(image[0])

            for i in range(4):

                new_x , new_y =sr + deltaRow[i] , sc + deltaCol[i]

                if new_x>=0 and new_x<m and new_y>=0 and new_y<n and image[new_x][new_y]==iniCol and ans[new_x][new_y]!=color:

                    dfs(new_x,new_y,image,ans,color,deltaRow,deltaCol,iniCol)


        ans=image
        deltaRow=[+1,0,-1,0]

        deltaCol=[0,+1,0,-1]

        iniCol=image[sr][sc]

        dfs(sr,sc,image,ans,color,deltaRow,deltaCol,iniCol)

        return ans
        