class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftmax=height[left]
        rightmax=height[right]
        water=0
        while left<=right:
            if leftmax<=rightmax:
                water+=min(leftmax,rightmax)-height[left]
                left+=1
                if height[left]>leftmax:
                    leftmax=height[left]
            else:
                water+=min(leftmax,rightmax)-height[right]
                right-=1
                if height[right]>rightmax:
                    rightmax=height[right]
        return water
        