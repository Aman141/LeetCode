class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = {}
        for i in nums:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i]+=1

        for i, j in dct.items():
            if j>=(len(nums)/2):
                return i            