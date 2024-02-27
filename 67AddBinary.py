class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lena = len(a)
        lenb = len(b)
        maxLenght = max(lena, lenb)
        output = []
        a = a[::-1]
        b = b[::-1]
        carry = 0
        result = []
        for i in range(0, maxLenght):
            bbit = 0
            abit = 0
            if i < lenb:
                bbit = int(b[i])
            if i < lena:
                abit = int(a[i])
            sum_ = bbit + abit + carry
            if sum_ > 1:
                carry = 1
                sum_ = sum_ - 2
            else:
                carry = 0
            result.append(sum_)
        if carry == 1:
            result.append(1)
        res = ''.join(str(i) for i in result)
        return res[::-1]


if __name__=='__main__':
    print(Solution().addBinary('11','1'))