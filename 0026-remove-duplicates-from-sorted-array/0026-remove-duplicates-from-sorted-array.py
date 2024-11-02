class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=list(set(nums))
        num.sort()
        for i in range(len(num)):
            nums[i]=num[i]
        return len(num)
        