class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # this code references the code of 'Solutions' on LeetCode
        st1, st2 = Counter(ransomNote), Counter(magazine)

        # compute the intersection of two Counters
        # the intersection includes only the common characters and takes the minimum count for each
        return st1 & st2 == st1
