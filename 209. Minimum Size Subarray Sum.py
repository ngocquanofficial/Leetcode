class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_len = n
        first = 0
        second = 0
        current_sum = nums[0]
        if sum(nums) < target :
            return 0
        while first <= n-1 :
            # Now current_sum is the minimun possible sum start from first pointer
            
            # loop through second
            while True :
                if current_sum >= target :
                    # satisfy the problem
                    current_len = second - first + 1
                    if current_sum < min_len :
                        min_len = current_len
                    
                    # now break the while loop
                    break

                # ELSE current_sum < target, need more element in subarray
                if second <= n-2 :
                    second += 1
                    current_sum += nums[second]
                    current_len = second - first + 1
                    continue
                
                # ELSE :
                break
            
            # Check last time 
            if current_sum >= target and current_len < min_len :
                min_len = second - first + 1
            
            # move to the next index
            current_sum -= nums[first]
            first += 1

        return min_len




            

target = 11
nums = [1,2,3,4,5]
obj = Solution()
print(obj.minSubArrayLen(target, nums))


