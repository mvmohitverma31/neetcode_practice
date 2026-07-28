class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fin=[]
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        sort=list(freq.items())
        for j in range(len(sort)-1):
            for i in range(len(sort)-1):
                if sort[i][1]>sort[i+1][1]:
                    sort[i],sort[i+1]=sort[i+1],sort[i]
        if k!=0:
            for i in range(1,k+1):
                o=sort[-i][0]
                fin.append(o)
                k-=1
                if k==0:
                    break
        return fin