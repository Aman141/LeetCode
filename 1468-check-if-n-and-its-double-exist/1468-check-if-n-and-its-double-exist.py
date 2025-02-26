class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dct = {}
        count = 0
        for i in range(len(arr)):
            if arr[i]==0:
                count+=1
                if count == 2:
                    return True
                continue
            if arr[i]*2 in dct.keys() or (arr[i]%2==0 and arr[i]//2 in dct.keys()):
                return True
            dct[arr[i]] = i
        return False    
                
        