class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        po=nums[0]
        li=set()
        for _ in range(len(nums)):
            li.add(po)
            if po+1 in nums:
                li.add(po+1)
                po=po+1
        return len(li)

