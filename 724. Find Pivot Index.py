class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        n = len(nums)
        if total_sum - nums[0] == 0 : # special case when sum(nums[1:]) = 0
            return 0
        for i in range(1, n) :
            if 2 * sum(nums[:i]) + nums[i] == total_sum :
                return i
        return -1
    