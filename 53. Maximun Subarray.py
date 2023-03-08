class Solution:
    def maxSubArray(self, nums):
        # Solve by dynamic programming
        # s[i] is the maximun subarray whose ending elements is nums[i]
        s = [0] * len(nums)
        s[0] = nums[0]
        for i in range(1, len(nums)) :
            if s[i-1] > 0 :
                s[i] = nums[i] + s[i-1]
            else :
                s[i] = nums[i]

        return max(s)