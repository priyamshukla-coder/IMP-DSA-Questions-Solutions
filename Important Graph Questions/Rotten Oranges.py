class Solution:
        
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows,cols=len(grid),len(grid[0])

        def check_valid_cell(row,col):

            return True if 0<=row<rows and 0<=col<cols else False
        
        q1=deque()

        fresh=0

        for i in range(rows):

            for j in range(cols):

                if grid[i][j]==2:

                    q1.append([i,j,0])

                elif grid[i][j]==1:

                    fresh+=1

        # print(q1,fresh)

        min_time=0

        directions=[(1,0),(-1,0),[0,1],[0,-1]]

        while len(q1)>0:

            x,y,t=q1.popleft()

            for dir in directions:

                new_x,new_y=x+dir[0],y+dir[1]

                if check_valid_cell(new_x,new_y) and grid[new_x][new_y]==1:

                    q1.append([new_x,new_y,t+1])

                    grid[new_x][new_y]=2

                    min_time=t+1

                    fresh-=1

                    # print(min_time)
        
        return min_time if fresh==0 else -1
