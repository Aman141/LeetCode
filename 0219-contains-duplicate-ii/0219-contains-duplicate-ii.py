class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}

        for i in range(len(nums)):
            if nums[i] in dct:
                return True
            dct[nums[i]] = i
            if len(dct)>k:
                del dct[nums[i-k]]

        return False                    
