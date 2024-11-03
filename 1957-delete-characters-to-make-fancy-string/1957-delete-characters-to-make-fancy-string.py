class Solution:
    def makeFancyString(self, s: str) -> str:
        new_str = s[0]
        count = 1
        for i in range(1,len(s)):
            if new_str[-1] == s[i]:
                count+=1
                if(count<3):
                    new_str+=s[i]
            else:
                count=1
                new_str+=s[i]

        return new_str