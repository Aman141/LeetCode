class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dct = {}
        for num in nums:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1

        for key,value in dct.items():
            if dct[key]%2:
                return False            
        
        return True