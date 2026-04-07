# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # use binary search
        # soring is unnecessary
        start = 1
        end = n

        while start <= end:
            mid = (start + end)//2

            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            elif isBadVersion(mid) == True:
                end = mid - 1
            else:
                start = mid + 1