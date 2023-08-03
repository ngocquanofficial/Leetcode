class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        # ELSE nums > 2 elements

        max_array = [0] * len(nums)
        # max_array[i] store the maximum amout of money if robber only rob from 0 to i-th house
        # Base case
        max_array[0] = nums[0]
        max_array[1] = max(nums[0], nums[1])
        current_max = max(max_array[0], max_array[1])

        for idx in range(1, len(nums)):
            # If the robber rob at the idx house, then it can not rob the idx-1 house
            # As a result, the maximum is max_array[idx - 2 ] + nums[idx]
            contain_idx_house = max_array[idx - 2] + nums[idx]
            # If the robber do not rob at the idx house, then the maximun is the same as
            # max_array[idx - 1]
            without_idx_house = max_array[idx - 1]
            max_array[idx] = max(contain_idx_house, without_idx_house)

            if max_array[idx] > current_max:
                current_max = max_array[idx]
        return current_max
