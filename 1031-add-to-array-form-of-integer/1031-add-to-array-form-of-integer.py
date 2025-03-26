class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        for i in range(len(num)-1,-1,-1):
            if k == 0 and carry==0:
                break
            t = num[i] + k%10 + carry    
            num[i] = (t)%10
            carry = t//10
            k = k//10

        if carry!=0 or k!=0:
            ans = []
            s = carry + k
            print(s)
            while(s):
                print(s%10)
                ans.append(s%10)
                s = s//10
            return ans[::-1] + num

        return num