class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal): return False
        if s == goal: return True
        start_i = []
        l = len(s)
        for i in range(l):
            if goal[i] == s[0]:
                start_i.append(i)

        if len(start_i)==0:
            return False
        
        for i in start_i:
            if goal[i:]==s[:l-i] and goal[:i]==s[l-i:]:
                return True    
  

        return False        



        