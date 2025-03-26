class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len_inc = 1
        max_len_dec = 1
        curr_dec = 1
        curr_inc = 1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                curr_dec +=1
                max_len_inc = max(max_len_inc, curr_inc)
                curr_inc = 1

            elif nums[i]>nums[i-1]:
                curr_inc += 1
                max_len_dec = max(max_len_dec, curr_dec)
                curr_dec = 1
            else:
                max_len_inc = max(max_len_inc, curr_inc)
                max_len_dec = max(max_len_dec, curr_dec)   
                curr_dec = 1
                curr_inc = 1    
        max_len_inc = max(max_len_inc, curr_inc)
        max_len_dec = max(max_len_dec, curr_dec)            
        return max(max_len_dec, max_len_inc)        




        