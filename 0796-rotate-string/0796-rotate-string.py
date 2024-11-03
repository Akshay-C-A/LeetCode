class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            rot_str = s[i:] + s[:i]
            if(rot_str==goal):
                return True
        return False
        