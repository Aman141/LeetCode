class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 2
        for i in range(2,len(nums)):
            if nums[i]!=nums[a-2]:
                nums[a] = nums[i]
                a+=1



        return a    
        