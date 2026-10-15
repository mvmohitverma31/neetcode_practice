class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            s="".join(sorted(i))
            if s not in dic:
                dic[s]=[]
            dic[s].append(i)
        return list(dic.values())