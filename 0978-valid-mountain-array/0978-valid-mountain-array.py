class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        if arr[1]<arr[0]:
            return False
        else:
            top_seen = False
            for i in range(0, len(arr)-1):
                if arr[i+1]>arr[i] and not top_seen:
                    continue
                elif arr[i+1]<arr[i] and not top_seen:
                    top_seen = True
                    continue
                elif arr[i+1]<arr[i] and top_seen:
                    continue
                else:
                    return False
            return True and top_seen    
                
        