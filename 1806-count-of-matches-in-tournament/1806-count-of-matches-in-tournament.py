class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """

        teamCnt = 0
        tmp = 0
        
        while n > 1:
            print(n)

            if n % 2 == 1:
                n -= 1
                tmp = 1
            else:
                tmp = 0
            
            teamCnt += n//2
            n = n//2 + tmp

        return teamCnt