class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        set_name = set(jewels)
        for ele in stones :
            if ele in set_name :
                count += 1
        return count
        