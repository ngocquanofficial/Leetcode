class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while right > left + 1:
            mid = (left + right) // 2

            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid

        # base case
        if right == left + 1:
            return min(nums[left], nums[right])
        return nums[mid]


nums = [11, 13, 15, 17]
obj = Solution()
print(obj.findMin(nums))
