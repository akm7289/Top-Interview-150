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
        lst = lst[::-1]
        for i in range(len(lst)):
            result = result + lst[i] * (2 ** i)

        return result
