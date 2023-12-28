class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # The highest altitude is the maximun sub-sum
        # which is the sum of a consecutive element starting from the first element
        max_sum = 0
        current_sum = 0
        for idx in range(len(gain)):
            current_sum += gain[idx]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
