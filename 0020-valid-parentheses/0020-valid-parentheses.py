class Solution:
    def isValid(self, s: str) -> bool:
        l=list(s)
        l2=[]
        match={')':'(',']':'[','}':'{'}
        for i in l:
            if i in ['(','[','{'] :
                l2.append(i)
            elif l2 and i in [')',']','}'] and l2[-1] == match[i]:
                l2.pop()
            else:
                return False


        if(l2==[]):
            return True
     
        