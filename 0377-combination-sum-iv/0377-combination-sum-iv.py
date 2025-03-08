class Solution:
    def combsum(self, nums, target, maps= None) ->int:
        if maps is None:
            maps = {}
        if target in maps:
            return maps[target]
        if target < 0 : return 0
        if target == 0: return 1

        count = 0
        for num in nums:
            target_new = target - num
            a = self.combsum(nums, target_new, maps)
            count +=a

        maps[target] = count
        return count  

    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.combsum(nums,target)





        
 