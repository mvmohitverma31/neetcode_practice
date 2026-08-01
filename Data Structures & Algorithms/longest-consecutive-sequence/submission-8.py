class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        best=0
        if nums!=[]:
            for i in nums:
                count=0
                if i-1 not in nums:
                    val=i
                    count+=1
                    while val+1 in nums:
                        if val+1 in nums:
                            count+=1
                            val+=1
                        if count>best:
                            best=count

            return best
