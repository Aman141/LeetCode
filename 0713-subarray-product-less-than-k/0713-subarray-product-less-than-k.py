class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        prod = 1   
        count = 0
        j = 0
        for i in range(len(nums)):
            prod = prod * nums[i]
            while prod>=k:
                prod //= nums[j]
                j +=1

            count += i-j+1    


        return  count