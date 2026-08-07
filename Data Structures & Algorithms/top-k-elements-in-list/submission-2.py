class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        fin=[]
        b=1
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]=b+1
            else:
                freq[nums[i]]=b

        while k!=0:
            maxx=0
            for i in freq:
                if i not in fin:
                    if freq[i]>=maxx:
                        maxx=i
            fin.append(maxx)
            k-=1
        return fin