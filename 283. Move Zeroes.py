class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        total_zeros = 0
        for i in range(n):
            if nums[i] == 0:
                total_zeros += 1
                continue
            nums[i - total_zeros] = nums[i]

        for i in range(n - total_zeros, n):
            nums[i] = 0
