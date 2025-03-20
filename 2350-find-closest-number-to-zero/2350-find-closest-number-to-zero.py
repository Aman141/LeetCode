class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_distance = 1000000
        ans = nums[0]
        for i in nums:
            if abs(i)<min_distance :
                min_distance = abs(i)
                ans = i
            if abs(i)==min_distance:
                if i>ans:
                    ans = i
        return ans