class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dct = {}

        for i in range(len(arr)):
            if arr[i]*2 in dct.keys() or (arr[i]%2==0 and arr[i]//2 in dct.keys()):
                return True
            dct[arr[i]] = i
        return False    
                
        