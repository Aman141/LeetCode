class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p, q = 0,0
        ans = ""
        while(p<len(word1) and q < len(word2)):
            ans += word1[p]
            p = p+1
            ans += word2[q]
            q = q+1


        ans += word2[q:]
        ans += word1[p:]

        return ans                   

        