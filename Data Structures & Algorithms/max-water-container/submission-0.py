class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        for i in range(len(heights)):
            width=r-l
            high=min(heights[l],heights[r])
            area=width*high
            if heights[l]<heights[r]:
                l+=1
            elif heights[r]>heights[l]:
                r+=1
        return area