class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ""
        op = 0
        result = []
        for char in s:
            if char == '(':
                op += 1   
            elif char == ')' :
                if op == 0:
                    continue
                op -= 1
            result.append(char)

        if op>0:
            new_result = []
            for i in range(len(result)-1,-1,-1):
                if result[i] =='(' and op!=0:
                    op -= 1
                    continue
                new_result.append(result[i])   
   
            return ''.join(reversed(new_result))
        return ''.join(result)        
        