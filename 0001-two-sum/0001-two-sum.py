class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if nums[i] in dct:
                return [i, dct[nums[i]]]
            else:
                dct[temp] = i
        
        return dct