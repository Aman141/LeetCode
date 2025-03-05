class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = strs[0]
        if ans == "":
            return ""

        for st in (strs[1:]):
            if st == "":
                return ""
            for j in range(len(st)):
                if j> len(ans)-1:
                    break
                if st[j]==ans[j]:
                    continue
                else:
                    ans = ans[:j]
                    break
            if ans == "":
                return ans
            if j == len(st)-1:
                ans = ans[:j+1]
        
        return ans                

               
        