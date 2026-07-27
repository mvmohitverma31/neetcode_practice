class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            M=target-nums[i]
            if M in seen:
                return [seen[M],i]
            seen[nums[i]]=i