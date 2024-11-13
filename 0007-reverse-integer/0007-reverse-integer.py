class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        arr = []
        count = 0
        temp = abs(x)
        while (temp):
            rev = 10*rev+temp%10

            count +=1
            temp = temp//10

        if(x<0): rev = -1*rev
        if(rev>(2**31)-1): return 0
        if(rev<(-2**31)): return 0 
        return rev
        