class Solution:
    def productExceptSelf(self, nums):
        product_array = [1] * len(nums)
        product_array[0] = 1
        product_array[1] = nums[0]
        # Base case
        if len(nums) == 2:
            return [nums[1], nums[0]]

        # After for loop, # product_array[i] store the product of element from index 0 to the index i - 1
        for i in range(2, len(nums)):
            product_array[i] = product_array[i - 1] * nums[i - 1]

        current_const = 1
        # After second for loop we got the final output
        for i in range(len(nums) - 2, -1, -1):
            current_const *= nums[i + 1]
            product_array[i] *= current_const

        return product_array
