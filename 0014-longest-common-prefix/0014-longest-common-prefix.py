class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        # Take the first string as the initial prefix
        prefix = strs[0]
        prefix_length = len(prefix)

        for s in strs[1:]:
            if not s:  # If any string is empty, return empty prefix
                return ""
            
            # Compare characters one by one
            j = 0
            while j < prefix_length and j < len(s) and prefix[j] == s[j]:
                j += 1
            
            # Update prefix length
            prefix_length = j
            
            # If at any point prefix becomes empty, return immediately
            if prefix_length == 0:
                return ""

        return prefix[:prefix_length]              

               
        