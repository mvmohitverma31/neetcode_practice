class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            l=0
            r=len(numbers)-1
            temp=[]
            while temp==[]:
                rem=numbers[l]+numbers[r]
                if rem==target:
                    temp=[l+1,r+1]
                elif rem>target:
                    r-=1
                elif rem<target:
                    l+=1
            return temp
