class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        lst = []
        while n > 0:
            remainder = n % 2
            n //= 2
            lst.append(remainder)
        result = 0
        lst.extend([0] * (32 - len(lst)))

        result = 0
        for i in range(len(lst)):
            result = (result << 1) | lst[i]

        return result
