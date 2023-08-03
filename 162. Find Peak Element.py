class Solution:
    def findPeakElement(self, nums):
        # We must find a local maximun point
        # We store 2 pointer first and last, in every step, we can guarantee that
        # there is at least 1 local maximun point between them
        first = 0
        last = len(nums) - 1
        mid = (first + last) // 2

        # Base case :
        if len(nums) == 1:
            return 0

        # At the begining the array must increase, ending must decrease, else there exist a
        # peak due to the constraint
        if nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1

        while last > first + 1:
            mid = (first + last) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                # Then mid is a peak
                return mid
            elif nums[mid] < nums[mid + 1]:
                first = mid
            else:
                last = mid
