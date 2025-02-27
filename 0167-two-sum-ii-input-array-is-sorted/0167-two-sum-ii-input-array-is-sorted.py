class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(numbers)):
            a = (target-numbers[i])
            if a in s.keys():
                return sorted([i+1, s[a]])
            else:
                s[numbers[i]] = i+1    

        return 