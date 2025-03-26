class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        dct_1 = Counter(nums1)
        dct_2 = Counter(nums2)

        ans = []

        for key in dct_1:
            if key in dct_2:
                min_c = min(dct_1[key], dct_2[key])
                ans += [key]*min_c

        return ans
        