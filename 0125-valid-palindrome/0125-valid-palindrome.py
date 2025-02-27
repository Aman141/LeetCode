class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = []
        for i in s:
            if i.isalnum():
                clean_s.append(i)
        l = 0
        r = len(clean_s)-1
        while(l<=r):
            if clean_s[l].lower() != clean_s[r].lower():
                return False
            l+=1
            r-=1    

        return True        
        