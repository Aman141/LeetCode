class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]  # Add the current digit of `num` to `k`
                num[i] = k % 10  # Update `num[i]` with the last digit
                i -= 1
            else:
                num.insert(0, k % 10)  # Insert remaining digits at the front
            k //= 10  # Remove the last digit from `k`

        return num

        return num