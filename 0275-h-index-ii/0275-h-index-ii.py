class Solution:
    def hIndex(self, citations: List[int]) -> int:

        h = 0 
        for i in range(len(citations)-1,-1,-1):
            if h>=citations[i]:
                return h
            h += 1

        return h         

        