class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        p = sorted(p)

        for i in range(len(s)-len(p)+1):
            tmp = sorted(s[i:i+len(p)])

            if tmp == p:
                ans.append(i)

        return ans