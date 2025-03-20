class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1 
        if abs(x)==1 : 
            if not n%2 and x<0:
                return -x
            else:
                return x    
        abs_n = abs(n)

        prev, curr = 1,x 

        for i in range(2, abs_n+1):
            temp = curr
            curr = (x*curr)
            if curr == 0: 
                return 0
            if curr>100000 and n<0:
                return 0    
            prev = temp

        if n>0:
            return curr
        else:
            return 1/curr      
        