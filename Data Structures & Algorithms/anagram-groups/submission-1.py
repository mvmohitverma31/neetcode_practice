class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            sort=[]
            fin=[]
            freq={}
            for i in strs:
                s="".join(sorted(i))
                if s not in sort:
                    sort.append(s) 
                if i not in freq:
                    freq[i]=s
            for i in range(len(sort)):
                l=[]
                for j in freq:
                    if sort[i]==freq[j]:
                        l.append(j)
                if l not in fin:           
                    fin.append(l)
            return fin
        