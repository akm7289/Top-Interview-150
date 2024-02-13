class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        max_seq = 1
        min_ = max_ = nums[0]
        set_ = set()
        for i in nums:
            set_.add(i)
        for j in nums:
            currentSeq = 1
            nextNum = j
            prevNum = j
            while True:
                nextNum = nextNum + 1
                if nextNum in set_:
                    set_.remove(nextNum)
                    currentSeq += 1
                else:
                    break
            while True:
                prevNum = prevNum - 1
                if prevNum in set_:
                    currentSeq += 1
                    set_.remove(prevNum)
                else:
                    break
            if currentSeq > max_seq:
                max_seq = currentSeq
        return max_seq


