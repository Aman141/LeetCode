class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        sum_list = [0]*(len(nums)+1)
        for i in queries:
            sum_list[i[0]] += 1
            sum_list[i[1]+1] -= 1

        curr = 0
        for a in range(len(nums)):
            curr += sum_list[a]
            if nums[a]-curr>0:
                return False
        return True
        