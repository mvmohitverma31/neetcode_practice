class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxx=0
        while l<r:
            width=r-l
            high=min(height[l],height[r])
            area=width*high
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            maxx=max(maxx,area)
        return maxx