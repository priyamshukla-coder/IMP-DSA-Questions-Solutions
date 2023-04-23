class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        
        return abs(24-(arrivalTime+delayedTime)) if arrivalTime+delayedTime>=24 else arrivalTime+delayedTime