class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 1 
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] and count == 0:
                nums[a] = nums[i]
                a +=1
                count = 1
            elif nums[i] == nums[i-1] and count == 1:
                nums[a] = nums[i]
                a += 1
                count = 0
            elif nums[i] != nums[i-1] and count == 1:
                nums[a] = nums[i]
                a+=1
            else:
                continue        

        return a    
        