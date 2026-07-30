class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        k=1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j!=i:
                    k*=nums[j]
            res.append(k)
            k=1
        return res