class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        op = 0  # Tracks open parentheses
        
        # First pass: Remove extra closing parentheses
        for char in s:
            if char == '(':
                op += 1   
            elif char == ')':
                if op == 0:
                    continue  # Skip extra ')'
                op -= 1
            result.append(char)

        # Second pass: Remove extra opening parentheses
        new_result = []
        for char in reversed(result):
            if char == '(' and op > 0:
                op -= 1  # Skip extra '('
                continue
            new_result.append(char)

        return ''.join(new_result[::-1])  # Efficiently reverse back
