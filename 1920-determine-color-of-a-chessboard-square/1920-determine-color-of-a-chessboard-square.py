class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alpha = ord(coordinates[0])
        intt = int(coordinates[1])
        
        print(alpha + intt)
        if not (alpha + intt)%2:
            return False

        return True    