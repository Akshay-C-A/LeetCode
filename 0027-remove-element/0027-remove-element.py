class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num=nums[:]
        for i in num:
            if i==val:
                nums.remove(i)
        return len(nums)        