class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        firstIndex = 0
        secondIndex = 1
        minVal = nums[0] - 1
        while (secondIndex < len(nums)):
            if nums[firstIndex] == nums[secondIndex]:
                if secondIndex - firstIndex > 1:
                    secondIndex = firstIndex + 2
                    while (secondIndex < len(nums) and nums[firstIndex] == nums[secondIndex]):
                        nums[secondIndex] = minVal
                        secondIndex += 1
                    firstIndex = secondIndex

            else:
                firstIndex = secondIndex
            secondIndex += 1
        swapSize = 0
        for i in range(len(nums)):
            if nums[i] == minVal:
                swapSize += 1
            elif swapSize > 0:
                nums[i - swapSize] = nums[i]

        return len(nums) - swapSize



