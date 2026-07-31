class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-1):
            if nums[i]+1 in nums:
                count+=1
        return count
