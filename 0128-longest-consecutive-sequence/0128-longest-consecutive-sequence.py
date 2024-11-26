class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))
        longest = 1
        streak = 1

        for i in range(1,len(nums)):
            if( nums[i] == nums[i-1]+1):
                streak+=1
            else:
                longest=max(streak,longest)
                streak=1
        return max(streak,longest)
            



     