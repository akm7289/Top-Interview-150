class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        for i in range(len(digits)-1,-1,-1):
            tmp=carry+digits[i]
            if tmp>9:
                carry=1
                digits[i]=tmp-10
            else:
                digits[i]=tmp
                carry=0
                break
        if carry==1:
            digits.insert(0,1)
        return digits
if __name__=='__main__':
    print(Solution().plusOne([9]))