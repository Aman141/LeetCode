class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct = {}
        values = set()
        for i in range(len(s)):
            if s[i] in dct.keys():
                if dct[s[i]]!=t[i]:
                    return False
            if s[i] not in dct.keys():
                if t[i] in values:
                    return False
                dct[s[i]] = t[i]
                values.add(t[i])

        return True            


        