class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            sort=[]
            fin=[]
            freq={}
            for i in strs:
                l=[]
                s="".join(sorted(i))
                for j in strs:
                    m="".join(sorted(j))
                    if s==m:
                        l.append(j)
                if l not in fin:
                    fin.append(l)
            return fin