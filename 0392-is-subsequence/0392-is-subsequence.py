class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if t[i]==s[a]:
                a+=1
            if a == len(s):
                return True
        return False       
        