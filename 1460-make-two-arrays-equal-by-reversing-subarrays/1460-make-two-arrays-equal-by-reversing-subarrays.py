class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # for i in target:
        #     if i in arr:
        #         arr.remove(i)
        # if arr==[] :
        #     return True
        # else:
        #     return False
        
        #use sort also
        return True if Counter(target) == Counter(arr) else False
