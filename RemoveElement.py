class Solution(object):
    """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    def swapwithLastElement(self, nums, val, firstIndex, lastIndex):
        while (lastIndex > firstIndex and nums[lastIndex] == val):
            lastIndex -= 1
        if lastIndex > firstIndex:
            nums[lastIndex], nums[firstIndex] = nums[firstIndex], nums[lastIndex]
        return lastIndex

    def removeElement(self, nums, val):
        index = 0
        lastIndex = len(nums) - 1
        for i in range((len(nums))):
            if nums[i] == val:
                last_indextmp = self.swapwithLastElement(nums, val, i, lastIndex)
                index += 1

        for i in range(len(nums)):
            if nums[i] == val:
                return i
        return len(nums)

