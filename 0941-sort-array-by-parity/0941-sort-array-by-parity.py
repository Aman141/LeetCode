class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        
        a = 0
        for i in range(len(nums)):
            if(nums[i]%2==0):
                temp = nums[a]
                nums[a]=nums[i]
                nums[i] = temp
                a+=1
                
        return nums
                
        