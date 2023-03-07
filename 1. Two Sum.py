class Solution:
    def twoSum(self, nums, target) :
        dict_nums = {}
        for i in range(len(nums)) :
            dict_nums[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in dict_nums :
                j = dict_nums[target - nums[i]]
                if i != j :
                    return [i, j]