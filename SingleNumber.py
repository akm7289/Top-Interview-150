class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] = True
            else:
                dictionary[i] = False
        for key, value in dictionary.items():
            if not value:
                return key


