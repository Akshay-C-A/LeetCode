class Solution:
    def isPalindrome(self, s: str) -> bool:
        reduced = [i.lower() for i in s if i.isalnum()]
        l=0
        r=len(reduced)-1
        while(l<r):
            if reduced[l]!=reduced[r]:
                return False
            else:
                l+=1
                r-=1
        return  True