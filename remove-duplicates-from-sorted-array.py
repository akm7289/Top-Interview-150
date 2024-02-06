class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        if not nums or len(nums) <= 1:
            return len(nums)
        arr.append(nums[0])
        for i in range(0, len(nums), 1):
            if arr[-1] == nums[i]:
                continue
            arr.append(nums[i])
        for i in range(len(arr)):
            nums[i] = arr[i]
        return len(arr)


