class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        while n > 0:
            if n % 2 == 1:
                counter += 1
            n = n // 2
        return counter

