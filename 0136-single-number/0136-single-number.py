class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        exor=0
        for i in nums:
            exor^=i
        return exor