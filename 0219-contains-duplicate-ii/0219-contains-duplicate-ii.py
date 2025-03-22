class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dct = {}

        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = i
            else:
                if abs(dct[nums[i]]-i)<=k:
                    return True
                if abs(dct[nums[i]]-i)>k:
                   dct[nums[i]] = i

        return False                    
