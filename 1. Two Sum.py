# class Solution:
#     def twoSum(self, nums, target) :
#         dict_nums = {}
#         for i in range(len(nums)) :
#             dict_nums[nums[i]] = i
#         for i in range(len(nums)):
#             if target - nums[i] in dict_nums :
#                 j = dict_nums[target - nums[i]]
#                 if i != j :
#                     return [i, j]



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = dict()
        for i, num in enumerate(nums) :
            if target - num in hash_map :
                # if target - num in hash_map, this means num is the second number
                return [hash_map[target - num], i]
            else : # not found target - num yet, then continue to discover, hope to see target - num in the future :)
                hash_map[num] = i
    
nums = [3,2,4]
target = 6
obj = Solution()
print(obj.twoSum(nums, target))











