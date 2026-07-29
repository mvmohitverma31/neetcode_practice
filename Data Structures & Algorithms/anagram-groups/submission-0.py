class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            freq={}
            fin=[]
            for i in strs:
                if i not in freq:
                    s="".join(sorted(i))
                    freq[i]=s
            for i in freq:
                l=[]
                for j in freq:
                    if j not in l and freq[i]==freq[j]:
                        l.append(j)
                if l not in fin:           
                    fin.append(l)
            return fin


        