class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        trainers.sort()
        
        players.sort()
        
        st=0
        
        end=0
        
        cnt=0
        
        while st<len(players) and end<len(trainers):
            
            if players[st]<=trainers[end]:
                
                # print(players[st])
                
                cnt=cnt+1
                
                st=st+1
                
            end=end+1
            

                
        return cnt
                
                
            
            