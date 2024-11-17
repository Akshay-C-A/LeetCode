class Solution:
    def isHappy(self, n: int) -> bool:
        new=set()
        while n!=1 and n not in new:
            new.add(n)
            n=sum(int(digit)**2 for digit in str(n))
        return n==1
            