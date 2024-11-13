class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        if(x==0):
            return True
        lst = []
        
        reverseNum, temp = 0 , x
        while(x>0):
            lastdig = x%10
            reverseNum = 10*reverseNum + lastdig
            x = x//10
        
        if(temp == reverseNum): return True
        
        return False
        