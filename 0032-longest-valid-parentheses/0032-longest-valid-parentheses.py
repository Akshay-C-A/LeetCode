class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        n = len(s)
        maxlen = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxlen = max(maxlen, i - stack[-1])
        return maxlen