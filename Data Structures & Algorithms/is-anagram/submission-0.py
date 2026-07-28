class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        if len(s)==len(t):
                for i in s:
                    if i in freq:
                        freq[i]+=1   
                    else:
                        freq[i]=1
                for j in t:
                    if j in freq:
                        freq[j]-=1
                    else:
                        return False
                for k in freq:
                    if freq[k]>0:
                        return False
                return True
        return False
