class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        # Find last element that >= nums[-1]
        if left == right:
            if target == nums[0]:
                return 0
            else:
                return -1
        while right > left + 1:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        # After while loop, right = left + 1, return the larger
        if nums[right] > nums[left]:
            ans = right
        else:
            ans = left

        if nums[0] < nums[-1]:
            # sorted array
            left_bound = 0
            right_bound = len(nums) - 1
        else:
            if target > nums[-1]:
                left_bound = 0
                right_bound = ans
            else:
                left_bound = ans + 1
                right_bound = len(nums) - 1

        while right_bound > left_bound + 1:
            mid = (left_bound + right_bound) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right_bound = mid
            else:
                left_bound = mid

        if nums[left_bound] == target:
            return left_bound
        elif nums[right_bound] == target:
            return right_bound
        else:
            return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
obj = Solution()
print(obj.search(nums, target))
