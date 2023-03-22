class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for i in range(len(flowerbed)):

            if flowerbed[i]==0:

                if (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):

                    flowerbed[i]=1

                    # print(flowerbed)

                    n=n-1

        return True if n<=0 else False