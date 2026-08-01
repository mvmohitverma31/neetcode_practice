class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        best=set()
        if nums!=[]:
            for i in nums:
                count=0
                if i-1 not in nums:
                    val=i
                    count+=1
                    for j in range(len(nums)):
                        if val+1 in nums:
                            count+=1
                            val+=1
                    best.add(count)

        return max(best)
