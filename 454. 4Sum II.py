class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        first_hashmap = dict()
        second_hashmap = dict()
        n = len(nums1)
        # USE HASHMAP, change to 0(n*2)
        for i in range(n) :
            for j in range(n) :
                first_key = nums1[i] + nums2[j] 
                second_key = - nums3[i] - nums4[j] 

                if first_key in first_hashmap :
                    first_hashmap[first_key] += 1
                else :
                    first_hashmap[first_key] = 1

                if second_key in second_hashmap :
                    second_hashmap[second_key] += 1
                else :
                    second_hashmap[second_key] = 1

        count = 0
        for key, value in first_hashmap.items() :
            if key in second_hashmap :
                count += first_hashmap[key] * second_hashmap[key]
        
        return count
        
nums1 = [1,-1]
nums2 = [-1,1]
nums3 = [-1,1]
nums4 = [1,-1]

obj = Solution()
print(obj.fourSumCount(nums1, nums2, nums3, nums4))