class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        a_minus_b = set()
        b_minus_a = set2
        union = set()
        # b\a = b - a ^ b
        for element in set1:
            if element in set2:
                # union.add(element), which mean:
                b_minus_a.remove(element)
            else:  # Not in
                a_minus_b.add(element)
        return [list(a_minus_b), list(b_minus_a)]
