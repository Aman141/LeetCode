class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = []
        max_len = 0
        for i in s:
            if i not in visited:
                visited.append(i)
            else:
                max_len = max(max_len, len(visited))
                n = visited.index(i)
                del visited[:n+1]
                visited.append(i)

        return max(max_len, len(visited))            
            


       
        