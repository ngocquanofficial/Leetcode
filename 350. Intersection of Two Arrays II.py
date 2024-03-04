class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = self.create_occur_dict(nums1)
        dict2 = self.create_occur_dict(nums2)
        output_dict = dict()
        for key in dict1 :
            if key not in dict2 :
                continue
            
            output_dict[key] = min(dict1[key], dict2[key])


        return_list = []
        for key in output_dict :
            return_list += [key] * output_dict[key]
        return return_list
            

    def create_occur_dict(self, nums) :
        my_dict = dict()
        for num in nums :
            if num not in my_dict :
                my_dict[num] = 1
            else :
                my_dict[num] += 1


        return my_dict
        