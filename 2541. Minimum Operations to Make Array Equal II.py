class Solution:
    
    def check_equal(self, nums1, nums2, k) :
        if sum(nums1) != sum(nums2) :
            return False
        remainder1 = list(map(lambda x: x % k, nums1))
        remainder2 = list(map(lambda x: x % k, nums2))
        if remainder1 != remainder2 :
            return False
        difference = [x - y for x, y in zip(remainder1, remainder2)]

        return True

    def minOperations(self, nums1, nums2, k):
        if k == 0 :
            if nums1 == nums2 :
                return 0
            else :
                return -1
        if not Solution.check_equal(self, nums1, nums2, k) :
            return -1

        difference = [abs(x - y) for x, y in zip(nums1, nums2)]
        times = (sum(difference) // k) // 2
        return times
        
            
        
        