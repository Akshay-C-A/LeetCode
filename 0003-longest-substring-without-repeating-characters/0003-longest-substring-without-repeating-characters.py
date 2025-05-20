class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,res=0,0
        substr = set()
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l+=1
            substr.add(s[r])
            res = max(res,r-l+1)
        return res