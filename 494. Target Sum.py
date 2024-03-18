class Solution(object):
    def __init__(self) :
        self.visited = {}
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        def find(i, target) :
            if i == n-1 :
                return int(nums[i] == target) + int(-nums[i] == target)
            
            if (i, target) in self.visited :
                return self.visited[(i, target)]
            
            # ELSE
            ans = find(i+1, target + nums[i]) + find(i+1, target - nums[i])
            self.visited[(i, target)] = ans

            return ans
        
        ans = find(0, target)
        return ans

nums = [1,1,1,1,1]
obj = Solution()
print(obj.findTargetSumWays(nums= nums, target= 3))
        