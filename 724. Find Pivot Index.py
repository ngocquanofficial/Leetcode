# class Solution:
#     def pivotIndex(self, nums):
#         total_sum = sum(nums)
#         n = len(nums)
#         if total_sum - nums[0] == 0 : # special case when sum(nums[1:]) = 0
#             return 0
#         for i in range(1, n) :
#             if 2 * sum(nums[:i]) + nums[i] == total_sum :
#                 return i
#         return -1
    
# Update: Second solution at 28/12/2023


class Solution:
    def pivotIndex(self, nums) -> int:
        total_sum = sum(nums) - nums[0]
        left_sum = 0
        right_sum = total_sum

        if total_sum == 0 :
            return 0

        for idx in range(1, len(nums)) :
            # nums[idx] is the pseudo pivot
            left_sum += nums[idx-1]
            right_sum -= nums[idx]
            if left_sum == right_sum :
                return idx
            
        return -1

nums = [-1,-1,0,1,0,-1]
obj = Solution()
print(obj.pivotIndex(nums))