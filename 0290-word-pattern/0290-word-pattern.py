class Solution:
    def strip_func(self, s:str)-> list:
        lst = []
        a = 0
        for i in range(len(s)):
            if s[i]!=" ":
                continue
            else:
                lst.append(s[a:i])
                a = i+1
        lst.append(s[a:])
        return lst            


    def wordPattern(self, pattern: str, s: str) -> bool:
        dct = {}
        s = self.strip_func(s)
        print((s))
        if len(pattern)!=len(s):
            return False

        values = set()    
        for i in range(len(s)):
            if pattern[i] in dct.keys():
                if dct[pattern[i]]!=s[i]:
                    return False

            if pattern[i] not in dct.keys():
                if s[i] in values:
                    return False

                dct[pattern[i]]= s[i]
                values.add(s[i])
        print(dct)
        return True                    

        