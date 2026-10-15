class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in range(len(strs)):
            s="".join(sorted(strs[i]))
            if s not in dic:
                dic[s]=[]
            dic[s].append(strs[i])
        return list(dic.values())