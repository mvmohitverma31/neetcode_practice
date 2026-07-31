class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        li=set()
        for i in range(len(nums)):
            if nums[i]+1 in nums:
                li.add(nums[i])
                li.add(nums[i]+1) 
            if len(nums)==1 and len(li)==0:
                    li.add(nums[0])
            
        return len(li)
