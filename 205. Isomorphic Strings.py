class Solution:
    def isIsomorphic(self, s, t):
        s = list(s)
        t = list(t) # convert s, t from strings to str lists
        
        domain = set(s)
        domain = list(domain) # the order is not important
        image = []
        
        for x in domain :
            index = s.index(x)
            image.append(t[index])
        
# Due to the condition 'No two characters may map to the same character'
        if len(image) != len(list(set(image))) :
            return False
        
        for i in range(len(s)) :
            x = s[i] # the domain point
            
            if t[i] != image[domain.index(x)] :
                return False
        
        return True
    
# 26.2.2024, code lại ý tưởng dùng domain-image
class Solution1:
    def isIsomorphic(self, s, t):
        set_s = set(s)
        set_t = set(t)

        map_dict = dict()

        for i, letter in enumerate(s) :
            if letter not in map_dict :
                map_dict[letter] = t[i] # map s[i] to t[i]
        
        # then create image of s using function map_dict, then compare with t
        image_string = ""
        for letter in s :
            image_string += map_dict[letter]
        
        # TO ENSURE THAT THERE ARE NO 2 LETTER MAP TO THE SAME IMAGE LETTER
        if len(map_dict.values()) > len(set(map_dict.values())) :
            return False
        
        return image_string == t
    
obj = Solution1()
s = "badc"
t = "baba"
print(obj.isIsomorphic(s, t))

        
class Solution2:
    # IDEA: From set A and set B with the same length ==> always find a bijective function from A to B

    def isIsomorphic(self, s, t):
        set_s = set(s)
        set_t = set(t)
        zipped_set = set(zip(s, t))

        # when len zipped_set = len set_s, it is ensure that zipped_set is a valid function
        # (not exist x such that f(x) have 2 values)

        # when len zipped_set = len set_s, it is ensure that there is no two letter map to the same letter

        # when 3 length equals, zipped_set create a bijective function from s to t
        return len(set_s) == len(set_t) == len(zipped_set)


