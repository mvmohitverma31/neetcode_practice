class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left=0
        current=1
        right=2
        while right<=len(flowerbed):
            if flowerbed[current]==0:
                if flowerbed[left]==0 and flowerbed[right]==0:
                    flowerbed[current]=1
                    n-=1
                else:
                    left+=1
                    current+=1
                    right+=1
            else:
                    left+=1
                    current+=1
                    right+=1
        if n==0:
            return True
        else:
            return False