class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0, count_1, count_2 = 0,0,0

        for i in nums:
            if i == 0: 
                count_0 +=1

            elif i == 1:
                count_1 += 1

            else:
                count_2 +=1

        for i in range(len(nums)):
            if i<count_0:
                nums[i]=0
            elif i>=count_0 and i<(count_0+count_1):
                nums[i] = 1

            else:
                nums[i] = 2
