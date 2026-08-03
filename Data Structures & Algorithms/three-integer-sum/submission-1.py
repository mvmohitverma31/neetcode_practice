class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        fin=[]
        for f in range(len(nums)-1):
            l=f+1
            r=len(nums)-1
            ch=0-nums[f]
            while l<r:
                temp=[]
                summ=nums[l]+nums[r]
                if summ>ch:
                    r-=1
                elif summ<ch:
                    l+=1
                else:
                    temp.append(nums[l])
                    temp.append(nums[r])
                    temp.append(nums[f])
                    l+=1
                    r-=1
                if temp!=[] and temp not in fin:
                    fin.append(temp)
        return fin



