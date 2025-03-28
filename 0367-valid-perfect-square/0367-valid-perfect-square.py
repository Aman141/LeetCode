class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num

        while(low<=high):
            mid = (low + high)//2
            a = mid * mid
            if a ==num: return True
            elif a<num:
                low = mid + 1
            else:
                high= mid - 1

        return False             
        