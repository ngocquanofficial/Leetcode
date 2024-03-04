class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        mapping = dict()
        mapping["a"] = []
        for string in strings :

            # BASE CASE
            if len(string) == 1 :
                mapping["a"].append(string)
                continue


            # WHEN STRING MORE THAN 1 LETTER

            ord_value = self.ord_tuple(string)
            if ord_value not in mapping :
                mapping[ord_value] = [string]
                continue

            #ELSE
            mapping[ord_value].append(string)

        # DEAL WITH BASE CASE
        if mapping["a"] == [] :
            del mapping["a"]

        return list(mapping.values()) 

    def ord_tuple(self, string) :
        ord_list = []
        first_letter = string[0]
        for letter in string :

            ord_list.append( (ord(letter) - ord(first_letter)) % 26 ) # due to contraint only lowercase
        return tuple(ord_list)

        