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
            val=0
            for i in freq:
                if i not in fin:
                    if freq[i]>=maxx:
                        maxx=freq[i]
                        val=i
            fin.append(val)
            k-=1
        return fin