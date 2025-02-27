class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(nums)
        nums = nums[::-1]
        ans = nums[0]
        
        sec_max_seen = False
        sec_max = ans
        for i in range(1, len(nums)):
            if nums[i]!=ans and not sec_max_seen:
                sec_max = nums[i]
                sec_max_seen = True
                
            elif nums[i]!=sec_max and sec_max_seen:
                return nums[i]
            else:
                continue
        return ans
            
                
        