class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        # Base case nums has only 1 element
        if len(nums) == 0:
            if nums[0] == target:
                return 0
            else:
                return -1
        while end > start + 1:  # Avoid base case: end = start + 1, then mid = start
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:  # nums[mid] < target
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
