class Solution:
    def strip(self, s:str) -> list:
        list_s = []
        a = 0
        b = 0
        word = ""
        for i in range(len(s)):
            if s[i]== " ":
                if word !="":
                    list_s.append(word)
                    word = ""
                continue
            else: 
                word += s[i]  
        if word!="":
            list_s.append(word)
        return list_s    

    def lengthOfLastWord(self, s: str) -> int:
        list_s = self.strip(s)
        last_word = list_s[-1]
        return len(last_word)
        