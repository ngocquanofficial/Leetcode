class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = len(nums) - 1
        current_sum = sum(nums)
        if current_sum < target :
            return 0
        while True :
            if current_sum - nums[first] - nums[second] >= target :
                current_sum = current_sum - nums[first] - nums[second]
                first += 1
                second -= 1
            
            elif current_sum - nums[first] >= target :
                current_sum = current_sum - nums[first]
                first += 1
            
            elif current_sum - nums[second] >= target :
                current_sum = current_sum - nums[second]
                second -= 1
            
            else :
                return second - first + 1



            
nums = [2,3,1,2,4,3]
target = 7

obj = Solution()

print(obj.minSubArrayLen(target, nums))