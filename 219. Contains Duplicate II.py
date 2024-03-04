class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # NOTE: Ensure that all element in window is different
        current_window = set(nums[:k])

        n = len(nums)

        # FIRST BASE CASE
        if k >=n :
            return len(nums) > len(set(nums))
        

        if len(set(current_window)) < k :
            return True
        
        # When n >= k+1

        for i in range(k, n) :
            if nums[i] in current_window :
                return True
            # ELSE

            current_window.add(nums[i])
            current_window.remove(nums[i-k])


        return False



nums = [1,2,3,4,5,4,6]
k = 10


obj = Solution()
print(obj.containsNearbyDuplicate(nums, k))
