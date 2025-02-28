class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        major = -1

        for i in nums:
            if count == 0 :
                major = i

            if i == major:
                count +=1

            else:
                count -=1

        return major                         