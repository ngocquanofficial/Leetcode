class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        number = len(flowerbed)
        total = 0 # count the total amount of space that can be planted
        # base case
        if n == 0 :
            return True
        # When n > 0
        if len(flowerbed) == 0 :
            return False
        if len(flowerbed) == 1 :
            if flowerbed[0] == 0 :
                return True
            else :
                return False
        if len(flowerbed) == 2 :
            if n >= 2 :
                return False
            if sum(flowerbed) == 0 :
                return True
            else :
                return False
            

        if flowerbed[0] + flowerbed[1] == 0 :
            total += 1
            flowerbed[0] = 1
        for i in range(1, number-1) : # Similarly, we not consider the last element
            if flowerbed[i-1] + flowerbed[i+1] + flowerbed[i] == 0 : # when i-1, i, and i+1 is not planted
                total += 1
                flowerbed[i] = 1 # consider location i-th as being planted
            if total >= n :
                return True
        if flowerbed[-2] == 0 and flowerbed[-1] == 0 :
            total +=1 
            flowerbed[-1] = 1

        if total >= n :
            return True
        else :
            return False
        
flowerbed = [1]
n = 0
solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))

