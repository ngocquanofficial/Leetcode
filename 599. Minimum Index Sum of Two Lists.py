class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        first_appear = dict()
        for i, string in enumerate(list1) :
            if string not in first_appear :
                first_appear[string] = i
        
        out_str = ""
        min_sum = len(list1) + len(list2)
        for i, string in enumerate(list2) :
            if string not in first_appear :
                continue

            # IF EXIST
            if i + first_appear[string] < min_sum :
                min_sum = i + first_appear[string]
                out_str = string
        
        return out_str


        
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]

obj = Solution()
print(obj.findRestaurant(list1, list2))
