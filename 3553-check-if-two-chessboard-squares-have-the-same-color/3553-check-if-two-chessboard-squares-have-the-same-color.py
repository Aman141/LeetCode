class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        cc_1 = ord(coordinate1[0]) + int(coordinate1[1])
        cc_2 = ord(coordinate2[0]) + int(coordinate2[1])

        if cc_1 % 2 == cc_2%2: return True
        return False