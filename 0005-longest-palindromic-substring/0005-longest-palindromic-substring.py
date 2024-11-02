class Solution:
    def longestPalindrome(self, s: str) -> str:
        l2 = []

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    l2.append(substring)
        return max(l2, key=len)


              
        