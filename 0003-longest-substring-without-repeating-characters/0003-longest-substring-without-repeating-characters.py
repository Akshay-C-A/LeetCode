class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=list(s)
        l2=[]
        for i in range(len(l)):
            l1=[]
            for j in range(i,len(l)):
                if l[j] not in l1:
                    l1.append(l[j])
                else:
                    break
            l2.append(l1)
        max=0
        for i in l2:
            if len(i)> max:
                max=len(i)
        return max
            
