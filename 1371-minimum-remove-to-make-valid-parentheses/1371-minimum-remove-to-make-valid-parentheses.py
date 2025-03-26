class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ""
        op = 0

        for st in s:
            if st == ')' and op == 0:
                continue
            elif st == '(':
                op += 1
                ans += st

            elif st == ')' :
                op -= 1
                ans += st        

            else:
                ans += st

        if op>0:
            new_ans = ""
            for i in range(len(ans)-1,-1,-1):
                if ans[i] =='(' and op!=0:
                    op -= 1
                    continue
                new_ans += ans[i]    
            return new_ans[::-1]
        return ans        
        