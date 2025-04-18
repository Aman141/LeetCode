class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        left, right = 0, min(k-1, len(s)-1)
        i = 1
        while left<=len(s)-1:
            s[left],s[right] = s[right], s[left]

            left +=1
            right -=1

            if (left >= right):
                left =  i*2*k
                right = min(left + k - 1, len(s)-1)
                i += 1 

        
        return "".join(s)          


        