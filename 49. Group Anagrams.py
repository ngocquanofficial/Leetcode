class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = dict()
        for string in strs :
            sorted_str = self.sort_str(string)
            if sorted_str in mapping :
                mapping[sorted_str].append(string)
                continue
            # ELSE
            mapping[sorted_str] = [string]

        return list(mapping.values())



    def sort_str(self, string) :
        return "".join(sorted(string))