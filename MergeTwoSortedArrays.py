class Solution(object):
    def merge(self, nums1, m, nums2, n):
        index = 0
        sortedArr = []
        index1=m-1
        lastIndex=len(nums1)-1
        index2=n-1

        while (index1 >= 0 and index2 >= 0):
            if nums1[index1] > nums2[index2]:
                nums1[lastIndex]=nums1[index1]
                index1 -= 1
                lastIndex-=1
            else:
                nums1[lastIndex]=nums2[index2]
                index2 -= 1
                lastIndex-=1

        while (index2>=0):
            nums1[lastIndex]=nums2[index2]
            index2 -= 1
            lastIndex-=1
        return nums1

