class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[a]=nums[i]
                a+=1
        print(a)
        for j in range(a, len(nums)):
            nums[j]=0
        return nums        
        