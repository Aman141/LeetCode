class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        left = 0
        right = len(s)-1
        s = list(s)
        while(left<=right):
            if s[left].lower() in vowels and s[right].lower() in vowels:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left +=1
                right -=1
                continue

            elif s[left].lower() in vowels:
                right -=1
                continue

            elif s[right].lower() in vowels:
                left +=1  
                continue      

            else:
                left +=1
                right -=1

        return "".join(i for i in s)        