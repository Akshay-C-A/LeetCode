class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if(nums[0]+nums[1]>nums[2]):
            if(nums.count(nums[0])==2 or nums.count(nums[1])==2):
                return "isosceles"
            elif(nums.count(nums[0])==3):
                return "equilateral"
            else:
                return "scalene"
        else:
            return "none"