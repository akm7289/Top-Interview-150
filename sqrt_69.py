class Solution(object):
    def mySqrt(self, x):
        l = 0
        h = x
        m=l

        if x<4 and x>0:
            return 1
        while l <= h:
            m = (l + h) // 2
            if m * m == x:
                return m
            elif m * m < x:
                if (m+1)*(m+1)>x:
                    return m
                l = m + 1
                continue
            else:
                h = m - 1
                continue
        return m
