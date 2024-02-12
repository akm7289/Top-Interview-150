class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        dic = {}
        set_ = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]

        prev = float('inf')
        pev2 = float('inf')
        for i in range(0, len(nums) - 2):
            if prev == nums[i]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if pev2 == nums[j]:
                    continue
                if -1 * (nums[i] + nums[j]) in dic:
                    for index in dic[-1 * (nums[i] + nums[j])]:
                        if index > j:
                            set_.add(tuple(sorted([nums[i], nums[j], nums[index]])))
                pev2 = nums[j]
            prev = nums[i]
        for s in set_:
            output.append(list(s))
        return output

