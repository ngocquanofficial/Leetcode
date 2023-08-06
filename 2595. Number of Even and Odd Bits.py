import math


class Solution:
    def evenOddBit(self, n):
        exponential = int(math.log2(n))
        # if exponential == int(exponential):
        #     exponential = int(exponential)
        # else:
        #     exponential = math.ceil(exponential)
        even = 0
        odd = 0
        status = exponential % 2  # 0 represent even position
        for i in range(exponential, -1, -1):
            coeff = n // (2**i)
            if coeff == 0:
                # ignore this case
                status = (1 + status) % 2
                continue
            # when coeff = 1

            if status % 2 == 0:
                even += 1
            else:
                odd += 1
            status = (1 + status) % 2
            n = n - coeff * 2**i

        return [even, odd]
