class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]+=1
            return digits

        carry = 1
        digits[-1] = 0
        for i in range(len(digits)-2, -1, -1):
            digits[i] += carry 
            if digits[i]//10:
                carry = 1 
                digits[i] = 0
            else:
                return digits

        if carry:
            digits.insert(0,1)   
            return digits       
