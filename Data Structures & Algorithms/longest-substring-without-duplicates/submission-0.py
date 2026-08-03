class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        maxx=0
        seen=set()
        while r<=len(s)-1:
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                if len(seen)>maxx:
                    maxx=len(seen)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
                r+=1
        return maxx