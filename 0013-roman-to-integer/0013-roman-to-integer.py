class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        visitI = False
        visitX = False
        visitC = False
        for i in s:
            if(i == 'I'):
                ans = ans+1
                visitI = True
            if (i == 'V'):
                if visitI:
                    ans = ans + 3
                else:    
                    ans = ans + 5
            if(i =='X'):
                visitX = True
                if visitI:
                    ans = ans+ 8
                if not visitI:
                    ans = ans+10
            if(i == 'L'):
                if visitX:
                    ans = ans + 30
                if not visitX:
                    ans = ans + 50
            if(i == 'C'):
                visitC = True
                if visitX:
                    ans = ans + 80
                if not visitX:
                    ans = ans + 100                
            if(i == 'D'):
                if visitC:
                    ans = ans + 300
                if not visitC:
                    ans = ans + 500   
         
            if(i == 'M'):
                if visitC:
                    ans = ans + 800
                if not visitC:
                    ans = ans + 1000                  
                
        return ans