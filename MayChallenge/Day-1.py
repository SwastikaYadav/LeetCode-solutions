# The isBadVersion API is already defined for you 
# @param version, an integer
# @return boolean
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        s, m, e = 1,1, n
        print(n)
        while s<=e:
            m=(s+e)//2
            if isBadVersion(m):
                e=m-1
            else:
                s=m+1
        return e+1
